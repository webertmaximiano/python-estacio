import numpy as np
from sklearn.preprocessing import MinMaxScaler

def normalize(data):
    # Remove colunas não numéricas
    numeric_data = data.select_dtypes(include=[np.number])

    scaler = MinMaxScaler()
    scaler.fit(numeric_data)

    normalized_data = scaler.transform(numeric_data)
    data[numeric_data.columns] = normalized_data

    return data
