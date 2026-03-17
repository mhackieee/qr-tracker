from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine('sqlite:///../data/logs.sqlite')

@app.route('/')
def index():
    try:
        df = pd.read_sql('scan_logs', engine)
        total = len(df)
        unique_env = df['Envelope_ID'].nunique()
    except: total, unique_env = 0,0
    return render_template('index.html', total=total, unique_env=unique_env)

@app.route('/scans')
def scans():
    df = pd.read_sql('scan_logs', engine)
    recent = df.sort_values('Device_Timestamp',ascending=False).head(50).to_dict(orient='records')
    return render_template('scans.html', scans=recent)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
