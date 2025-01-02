import pytest
import os
from src.data_ingestion import read_csv, read_json


@pytest.mark.parametrize("file_name", os.listdir("data/raw"))
def test_file_type_and_size(file_name):
    file_path = f"data/raw/{file_name}"
    file_size = os.path.getsize(file_path)
    
    # Check file size is not zero
    assert file_size > 0, f"{file_name} is empty."

    # Validate file type
    if file_name.endswith(".json"):
        read_json(file_path)  
    elif file_name.endswith(".csv"):
        read_csv(file_path) 
    else:
        pytest.fail(f"Unsupported file type: {file_name}")
