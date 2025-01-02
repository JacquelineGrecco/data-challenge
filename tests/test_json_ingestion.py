import pytest
from src.data_ingestion import read_json, validate_json_schema, read_schema

@pytest.mark.parametrize("file_name", ["allowance_events"])
def test_json_schema_validation(file_name):
    file_path = f"./data/raw/{file_name}.json" 
    data = read_json(file_path)
    allowance_events_schema = read_schema(file_name)
    for record in data.to_dict(orient="records"):
        validate_json_schema(record, allowance_events_schema)

