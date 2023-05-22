
from generate_schemas import run_schema_gen
from create_train_test_key_files import create_train_test_testkey_files
from generate_inference_data import generate_inference_request_data


if __name__ == "__main__":
    run_schema_gen()
    create_train_test_testkey_files()
    generate_inference_request_data()