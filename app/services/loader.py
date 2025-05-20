from pathlib import Path
from app.utils.reader import read_table
import pandas as pd

DATA_DIR = Path("data")

def list_datasets() -> list[str]:
    """Return a list of dataset filenames in the data directory."""
    allowed_exts = {".sas7bdat", ".xpt", ".csv", ".xlsx"}
    return [
        f.name
        for f in DATA_DIR.iterdir()
        if f.is_file() and f.suffix.lower() in allowed_exts
    ]


def load_dataset(name: str) -> pd.DataFrame:
    """Load a dataset by filename from the data directory."""
    file_path = DATA_DIR / name
    if not file_path.exists():
        raise FileNotFoundError(f"No such dataset: {name}")
    return read_table(str(file_path))
