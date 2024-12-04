import pytest
import pandas as pd 
import os

# Fixture to load the dataset 
@pytest.fixture(scope="module") 
def data_path(): 
    project_path = "/home/hgreger/Deploying-a-Scalable-ML-Pipeline-with-FastAPI" 
    data_path = os.path.join(project_path, "data", "census.csv") 
    return data_path
    
@pytest.fixture(scope="module")
def data(data_path): 
    return pd.read_csv(data_path)

# TODO: implement the first test. Change the function name and input as needed
def test_dataset_load(data):
    """
    Check if the dataset is properly loaded
    """
    assert not data.empty, "The dataset is empty."


# TODO: implement the second test. Change the function name and input as needed
def test_dataset_features(data):
    """
    Check if training features exist in the dataset
    """
    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]
    missing_features = [feature for feature in cat_features if feature not in data.columns]
    assert not missing_features, f"Missing columns from the dataset:{' '.join(missing_features)}"


# TODO: implement the third test. Change the function name and input as needed
def test_model_save():
    """
    Check if the model file exists
    """ 
    model_path = "./model/model.pkl" 
    assert os.path.isfile(model_path), "Model file does not exist."