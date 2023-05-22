import os
import json
import pandas as pd
import utils

def generate_inference_request_data():
    dataset_cfg_path = "./config/binary_classification_datasets_metadata.csv"
    processed_datasets_path = "./datasets/processed/"

    # Load the metadata
    dataset_metadata = utils.load_metadata(dataset_cfg_path)

    # Iterate through each dataset marked for use in the metadata
    for _, dataset_row in dataset_metadata[dataset_metadata['use_dataset'] == 1].iterrows():
        dataset_name = dataset_row["name"]
        print("Creating inference request data for dataset:", dataset_name)

        # Load the dataset
        dataset = utils.load_dataset(dataset_name, processed_datasets_path)

        # Cast id field to str
        dataset[dataset_row["id_name"]] = dataset[dataset_row["id_name"]].astype(str)

        # Extract the first row of the dataset, drop the target column, and convert to a dictionary
        sample_data = dataset.drop(columns=dataset_row["target_name"]).iloc[0].to_dict()

        # Convert numpy data types to native Python data types
        sample_data = utils.convert_numpy_types(sample_data)

        # Format the data for an inference request
        inference_request_data = {"instances": [sample_data]}

        # Write the inference request data to a JSON file
        output_path = os.path.join(
            processed_datasets_path, dataset_name, f"{dataset_name}_inference_request_sample.json")
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(inference_request_data, file, indent=2)


if __name__ == "__main__":
    generate_inference_request_data()

