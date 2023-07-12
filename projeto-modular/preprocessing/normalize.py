from sklearn.preprocessing import MinMaxScaler

def normalize(data):
    scaler = MinMaxScaler()
    scaler.fit(data)

    return scaler.transform(data)