import pandas as pd
import jsonschema
import json
from jsonschema import validate
from typing import Dict, Any

def read_csv(file_path: str) -> pd.DataFrame:
   
    """
    Reads a CSV file and returns a DataFrame.

    Args:
        file_path (str): Path to the CSV file to read.

    Returns:
        pd.DataFrame: DataFrame containing the data from the CSV file.

    Raises:
        ValueError: If there is an error reading the CSV file.
    """
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Error reading CSV file: {e}")
 
def read_schema(file_name: str) -> Dict[str, Any]:
    """
    Reads a JSON schema file and returns a dictionary.

    Args:
        file_name (str): Name of the file for which to read the schema.

    Returns:
        Dict[str, Any]: Dictionary containing the schema for the given file.

    Raises:
        ValueError: If there is an error reading the schema file.
    """
    file_schema_path = f"./data/schemas/{file_name}_schema.json"
    with open(file_schema_path, "r") as f:
        return json.load(f) 

def read_json(file_path: str) -> pd.DataFrame:
    """
    Reads a JSON file and returns a DataFrame.

    Args:
        file_path (str): Path to the JSON file to read.

    Returns:
        pd.DataFrame: DataFrame containing the data from the JSON file.

    Raises:
        ValueError: If there is an error reading the JSON file.
    """
    try:
        return pd.read_json(file_path)
    except Exception as e:
        raise ValueError(f"Error reading JSON file: {e}")

def validate_json_schema(data: Dict[str, Any], schema: Dict[str, Any]) -> None:
    """
    Validates the given data against the given JSON schema.

    Args:
        data (Dict[str, Any]): The data to be validated.
        schema (Dict[str, Any]): The JSON schema to validate against.

    Returns:
        None

    Raises:
        ValueError: If the data does not conform to the schema.
    """
    try:
        validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        raise ValueError(f"JSON schema validation error: {e}")
