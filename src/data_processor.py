import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataProcessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def process_data(self, data):
        df = pd.DataFrame([data])
        numeric_columns = ['temperature', 'vibration', 'pressure']
        df[numeric_columns] = self.scaler.fit_transform(df[numeric_columns])
        return df
