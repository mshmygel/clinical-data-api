import pandas as pd
import pyreadstat
from pathlib import Path


def read_table(file_path: str) -> pd.DataFrame:
    """Read a table file of supported format and return a Pandas DataFrame."""
    path = Path(file_path)
    ext = path.suffix.lower()

    if ext == ".sas7bdat":
        # df, _  -> df is DataFrame, _  is ignored metadata
        df, _ = pyreadstat.read_sas7bdat(path)
    elif ext == ".xpt":
        df, _ = pyreadstat.read_xport(path)
    elif ext == ".csv":
        df = pd.read_csv(path)
    elif ext in (".xls", ".xlsx"):
        df = pd.read_excel(path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

    return df
