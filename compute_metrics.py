import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///../data/logs.sqlite')

def load_logs():
    return pd.read_sql('scan_logs', engine, parse_dates=['Device_Timestamp','Server_Timestamp'])

def compute_retrieval_times(df):
    grp = df.sort_values(['Envelope_ID','Device_Timestamp']).groupby('Envelope_ID')
    results = []
    for env,g in grp:
        try:
            t_reg = g[g['Location_ID']=='REGISTER']['Device_Timestamp'].iloc[0]
            t_rel = g[g['Location_ID']=='RELEASE']['Device_Timestamp'].iloc[-1]
            results.append((env,(t_rel-t_reg).total_seconds()))
        except: pass
    return pd.DataFrame(results,columns=['Envelope_ID','retrieval_s'])

if __name__ == "__main__":
    df = load_logs()
    rt = compute_retrieval_times(df)
    print("Retrieval time summary (seconds):")
    print(rt['retrieval_s'].describe())
