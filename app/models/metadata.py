from pydantic import BaseModel
from typing import List, Any


class DatasetInfo(BaseModel):
    name: str
    rows: int
    columns: int


class ColumnInfo(BaseModel):
    name: str
    dtype: str
    nulls: int


class TablePreview(BaseModel):
    data: List[dict[str, Any]]
