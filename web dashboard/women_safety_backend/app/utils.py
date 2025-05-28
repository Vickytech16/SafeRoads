import json
import pandas as pd

def load_geojson(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_csv_data(path: str):
    return pd.read_csv(path)
