import pandas as pd
from preprocessing.normalize import normalize
from preprocessing.one_hot_encode import one_hot_encode

iris_dataset = pd.read_csv("./data/iris.csv")

normalize_data = normalize(iris_dataset)
encoded_data = one_hot_encode(iris_dataset)

print(normalize_data.head(5))
print("--------------------")
print(encoded_data.head(5))
