import pandas as pd

REQUIRED = {"id","x","y","z","a","b","c"}

def load_instances(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns in {csv_path}: {missing}")
    return df
