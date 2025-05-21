from fastapi import APIRouter, HTTPException
from app.services import loader
from app.models.metadata import DatasetInfo, ColumnInfo, TablePreview

router = APIRouter()


@router.get("/datasets", response_model=list[str])
def get_datasets():
    """List all available dataset filenames."""
    return loader.list_datasets()


@router.get("/datasets/{name}", response_model=DatasetInfo)
def get_dataset_info(name: str):
    """Return basic info about the dataset (rows, columns)."""
    try:
        df = loader.load_dataset(name)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return DatasetInfo(name=name, rows=len(df), columns=len(df.columns))


@router.get("/datasets/{name}/head", response_model=TablePreview)
def get_dataset_preview(name: str, limit: int = 10):
    """Return the first N rows of the dataset."""
    try:
        df = loader.load_dataset(name)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Dataset not found")
    preview = df.head(limit).to_dict(orient="records")
    return TablePreview(data=preview)


@router.get("/datasets/{name}/columns", response_model=list[ColumnInfo])
def get_dataset_columns(name: str):
    """Return column names, types, and null counts."""
    try:
        df = loader.load_dataset(name)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return [
        ColumnInfo(name=col, dtype=str(df[col].dtype), nulls=int(df[col].isnull().sum()))
        for col in df.columns
    ]
