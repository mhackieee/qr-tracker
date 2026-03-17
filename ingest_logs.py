import pandas as pd
import os
from sqlalchemy import create_engine

os.makedirs('../data', exist_ok=True)
engine = create_engine('sqlite:///../data/logs.sqlite')

def ingest(csv_path):
    df = pd.read_csv(csv_path, parse_dates=['Device_Timestamp','Server_Timestamp'])
    df.to_sql('scan_logs', engine, if_exists='append', index=False)
    print(f"Ingested {len(df)} rows into logs.sqlite")

if __name__ == "__main__":
    ingest('../sample_data/sample_scan_logs.csv')
