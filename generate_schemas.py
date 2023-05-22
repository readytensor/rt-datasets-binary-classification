import os
import pandas as pd
import json
from typing import Dict, List, Tuple
from utils import load_metadata, load_features_config, strip_quotes, JSONEncoder

processed_datasets_path = "./datasets/processed/"
features_cfg_path = "./config/binary_classification_datasets_fields.csv"


def create_feature_section(dataset_name: str, dataset_row: pd.Series, dataset: pd.DataFrame) -> List[Dict]:
    """
    Create the feature section of the schema.

    Args:
    dataset_name (str): The name of the dataset.
    dataset_row (pd.Series): The metadata for the dataset.
    dataset (pd.DataFrame): The dataset.

    Returns:
    List[Dict]: The features section of the schema.
    """
    # Filter features related to this dataset
    features_config = load_features_config(features_cfg_path)
    features_config = features_config.applymap(strip_quotes)
    features_config = features_config[features_config['name'] == dataset_row['name']]

    # create the features section
    features = []
    features_df = features_config[(features_config["name"]==dataset_name) & (features_config["field_type"]=="feature")]
    for _, feature_row in features_df.iterrows():
        feature = {
            "name": feature_row['field_name'],
            "description": feature_row['field_description'],
            "dataType": feature_row['data_type'].upper(),
        }
        if feature_row['data_type'].upper() == "CATEGORICAL":
            feature["categories"] = sorted(dataset[feature_row['field_name']].dropna().unique().tolist(), key=str)
        else:
            feature["example"] = dataset[feature_row['field_name']].dropna().iloc[0]
        feature["nullable"] = dataset[feature_row['field_name']].isnull().any()
        features.append(feature)

    return features


def generate_schemas(dataset_metadata: pd.DataFrame, processed_datasets_path: str):
    """
    Generate the schema for each dataset.

    Args:
    dataset_metadata (pd.DataFrame): The metadata for all the datasets.
    processed_datasets_path (str): The path where the processed datasets are stored.
    """
    schemas=[]
    dataset_names=[]

    # Iterate through all datasets marked for use in the metadata
    for _, dataset_row in dataset_metadata[dataset_metadata['use_dataset'] == 1].iterrows():

        dataset_name = dataset_row["name"]
        print("Creating schema for dataset", dataset_name)
        schema = dict()
        schema["title"] = dataset_row["title"]
        schema["description"] = dataset_row["description"]
        schema["modelCategory"] = dataset_row["model_category"]
        schema["schemaVersion"] = 1.0
        schema["inputDataFormat"] = "CSV"

        schema["id"] = {
            "name": dataset_row["id_name"],
            "description": dataset_row["id_description"]
        }

        schema["target"] = {
            "name": dataset_row["target_name"],
            "description": dataset_row["target_description"],
            "classes": dataset_row["target_classes"].split('|')
        }

        # read dataset
        dataset = pd.read_csv(os.path.join(
            processed_datasets_path, dataset_name, f"{dataset_name}.csv"))

        schema["features"] = create_feature_section(dataset_name, dataset_row, dataset)

        schemas.append(schema)
        dataset_names.append(dataset_name)

    # Write the schemas in JSON format to disk
    for dataset_name, schema in zip(dataset_names, schemas):
        output_fpath = os.path.join(
            processed_datasets_path,
            dataset_name,
            f"{dataset_name}_schema.json"
        )
        with open(output_fpath, "w", encoding="utf-8") as f:
            json.dump(schema, f, cls=JSONEncoder, indent=2)


def run_schema_gen():
    dataset_cfg_path = "./config/binary_classification_datasets_metadata.csv"
    dataset_metadata = load_metadata(dataset_cfg_path)
    generate_schemas(dataset_metadata, processed_datasets_path)


if __name__ == "__main__":
    run_schema_gen()
