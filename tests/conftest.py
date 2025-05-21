import shutil
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services import loader

@pytest.fixture
def client(tmp_path):
    # Create temporary /data directory
    test_data_dir = tmp_path / "data"
    test_data_dir.mkdir()

    # Copy test CSV file into it
    shutil.copy("tests/testdata/sample.csv", test_data_dir / "sample.csv")

    # Override global path used by the app
    loader.DATA_DIR = test_data_dir

    return TestClient(app)
