import yaml
import pandas as pd
import numpy as np
import os
import json
import pprint
from typing import Dict, Optional, Any


def read_yaml_file(file_path: str) -> Dict:
    """
    Reads a YAML file at the specified file path and converts it to a Python dictionary.

    Args:
        file_path: A string representing the path to the YAML file.

    Returns:
        A Python dictionary representing the contents of the YAML file.
    """
    with open(file_path, "r") as file:
        try:
            schema_dict = yaml.safe_load(file)
            return schema_dict
        except yaml.YAMLError as exc:
            print(exc)


def read_csv_file(dataset_name: str, data_dir: str = "./data") -> Optional[pd.DataFrame]:
    """
    Reads a CSV file for a specified dataset and returns the contents as a pandas DataFrame.

    Args:
        dataset_name: A string representing the name of the dataset.
        data_dir: A string representing the path to the directory where the CSV file is located.

    Returns:
        A pandas DataFrame representing the contents of the CSV file, or None if the file could not be found or read.
    """
    file_path = f"{data_dir}/{dataset_name}/processed/{dataset_name}.csv"
    if os.path.isfile(file_path):
        try:
            df = pd.read_csv(file_path)
            return df
        except Exception as e:
            print(f"Error reading CSV file '{file_path}': {e}")
            return None
    else:
        print(f"CSV file not found: '{file_path}'")
        return None


def save_schema_as_json(schema: Dict[str, Any], dataset_name: str, target_dir: str = "./schemas") -> None:
    """
    Saves a schema dictionary as a JSON file.

    Args:
        schema: A dictionary representing the schema for a dataset.
        dataset_name: A string representing the name of the dataset.
        target_dir: A string representing the path to the directory where the JSON file should be saved.
    """
    json_file = f"{target_dir}/{dataset_name}/processed/{dataset_name}_schema.json"
    try:
        with open(json_file, "w") as outfile:
            json.dump(schema, outfile, indent=2)
        # print(f"Schema JSON file saved at '{json_file}'")
    except Exception as e:
        print(f"Error saving schema JSON file '{json_file}': {e}")



def generate_schema(config: Dict[str, Any], data: pd.DataFrame) -> Dict[str, Any]:
    """
    Generates a schema dictionary based on the configuration and data input.

    Args:
        config: A dictionary representing the configuration for the dataset.
        data: A pandas DataFrame representing the input data.

    Returns:
        A dictionary representing the schema for the dataset.
    """
    id_field = config.get("idField")
    target_field = config.get("targetField")
    predictor_fields = config.get("predictorFields")
    
    # Generate schema for ID field
    id_schema = generate_id_schema(id_field)
    
    # Generate schema for target field
    target_schema = generate_target_schema(target_field, data)
    
    # Generate schema for predictor fields
    predictor_schemas = [generate_predictor_schema(field, data) for field in predictor_fields]
    
    # Construct final schema dictionary
    schema = {
        "title": config.get("title"),
        "description": config.get("description"),
        "problemCategory": config.get("problemCategory"),
        "version": config.get("version"),
        "inputDataFormat": config.get("inputDataFormat"),
        "idField": id_schema,
        "targetField": target_schema,
        "predictorFields": predictor_schemas
    }
    
    return schema


def generate_id_schema(id_field: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generates a schema dictionary for an ID field.

    Args:
        id_field: A dictionary representing the configuration for the ID field.

    Returns:
        A dictionary representing the schema for the ID field.
    """
    id_schema = {
        "name": id_field["name"],
        "description": id_field["description"]
    }

    return id_schema


def generate_target_schema(config: dict, data: pd.DataFrame) -> dict:
    """
    Generates a schema dictionary for the target field based on the configuration and data input.

    Args:
        config: A dictionary representing the configuration for the dataset.
        data: A pandas DataFrame representing the input data.

    Returns:
        A dictionary representing the schema for the target field.
    """
    target_field_config = config["targetField"]
    target_field_name = target_field_config["name"]
    unique_values = data[target_field_name].unique().tolist()

    target_schema = {
        "name": target_field_name,
        "description": target_field_config["description"],
        "allowedValues": [str(value) for value in unique_values],
    }

    if "positiveClass" in target_field_config:
        target_schema["positiveClass"] = target_field_config["positiveClass"]

    return target_schema




def generate_predictor_schema(predictor_field: dict, data: pd.DataFrame) -> dict:
    """
    Generates a schema dictionary for a predictor field.

    Args:
        predictor_field: A dictionary representing the configuration for the predictor field.
        data: A pandas DataFrame representing the input data.

    Returns:
        A dictionary representing the schema for the predictor field.
    """
    predictor_field_name = predictor_field["name"]
    
    # Get an example value from the input data for the predictor field
    example_value = data[predictor_field_name].dropna().iloc[0]
    if isinstance(example_value, (np.integer, np.floating)):
        example_value = example_value.tolist()  # Convert to native Python data type only for numeric types


    predictor_schema = {
        "name": predictor_field_name,
        "description": predictor_field["description"],
        "dataType": predictor_field["dataType"]
    }

    if predictor_field["dataType"] == "CATEGORICAL":
        unique_values = data[predictor_field_name].dropna().unique().tolist()
        predictor_schema["allowedValues"] = [str(value) for value in unique_values]
    elif predictor_field["dataType"] == "NUMERIC":
        predictor_schema["example"] = example_value

    return predictor_schema


       

def main() -> None:
    """
    Generates schema files for multiple datasets and saves them as JSON files.
    """
    # Read configuration file
    config_file_path = "./config2.yaml"
    config = read_yaml_file(config_file_path)
    
    # Loop over datasets and generate schema files
    datasets_dir = "./../datasets/"
    for dataset_name, dataset_config in config["datasets"].items():
        print(f"Running dataset_name {dataset_name}")

        # Read input data file
        data = read_csv_file(dataset_name = dataset_name, data_dir = datasets_dir)
        
        if data is not None:
            # Generate the schema for the dataset
            schema = {
                "title": dataset_config["title"],
                "description": dataset_config["description"],
                "problemCategory": config["problemCategory"],
                "version": config["version"],
                "inputDataFormat": config["inputDataFormat"],
                "idField": generate_id_schema(dataset_config["idField"]),
                "targetField": generate_target_schema(dataset_config, data),
                "predictorFields": [generate_predictor_schema(field, data) for field in dataset_config["predictorFields"]],
            }

            # Save the schema as a JSON file
            save_schema_as_json(schema, dataset_name, target_dir=datasets_dir)        
        


if __name__ == "__main__":
    main()
