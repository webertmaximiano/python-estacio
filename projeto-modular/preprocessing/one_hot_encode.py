import pandas as pd

def one_hot_encode(data):
    categorical_cols = data.select_dtypes(include=['object']).columns

    encoded_data = pd.get_dummies(data, columns=categorical_cols)

    return encoded_data
