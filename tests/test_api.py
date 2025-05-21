def test_get_datasets_returns_list_of_files(client):
    response = client.get("/datasets")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)

    for item in data:
        assert isinstance(item, str)
        assert item.lower().endswith((".csv", ".xlsx", ".xpt", ".sas7bdat"))


def test_get_datasets_returns_sample_csv(client):
    # Call the endpoint
    response = client.get("/datasets")

    # Basic checks
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert "sample.csv" in data

def test_get_dataset_info(client):
    response = client.get("/datasets/sample.csv")
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "sample.csv"
    assert data["rows"] == 2
    assert data["columns"] == 2

def test_get_dataset_columns(client):
    response = client.get("/datasets/sample.csv/columns")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert {"name": "id", "dtype": "int64", "nulls": 0} in data
    assert {"name": "name", "dtype": "object", "nulls": 0} in data

def test_get_dataset_head(client):
    response = client.get("/datasets/sample.csv/head")
    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert {"id": 1, "name": "Mike"} in data["data"]
    assert {"id": 2, "name": "Kit"} in data["data"]
