import pytest
from src.data_ingestion import read_csv

expected_columns = {
    "allowance_backend_table": ["uuid", "status", "next_payment_day"],
    "payment_schedule_backend_table": ["user_id", "payment_date"]
}

@pytest.mark.parametrize("file_name", ["payment_schedule_backend_table", "allowance_backend_table"])
def test_csv_columns_and_nulls(file_name):
    file_path = f"./data/raw/{file_name}.csv"
    df = read_csv(file_path)

    assert all(col in df.columns for col in expected_columns[file_name]), (
        f"{file_name} is missing required columns."
    )
    
    assert not df.isnull().any().any(), f"{file_name} contains null values."

    if "uuid" in df.columns:
        assert not df["uuid"].isnull().any(), f"{file_name} contains null values in 'uuid'."
    if "user_id" in df.columns:
        assert not df["user_id"].isnull().any(), f"{file_name} contains null values in 'user_id'."
