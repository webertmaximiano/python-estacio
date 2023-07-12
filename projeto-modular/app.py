import pandas as pd 
from preprocessing.normalize import *

iris_dataset = pd.read_csv("./data/iris.csv")

normalize_data = normalize(iris_dataset)

print(normalize_data.head(5))