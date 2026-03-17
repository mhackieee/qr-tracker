import pandas as pd
import numpy as np

def cronbach_alpha(df):
    item_vars = df.var(axis=0, ddof=1)
    total_var = df.sum(axis=1).var(ddof=1)
    n_items = df.shape[1]
    return (n_items/(n_items-1))*(1-item_vars.sum()/total_var)

if __name__ == "__main__":
    df = pd.read_csv('../sample_data/sample_questionnaire.csv')
    items = df[[c for c in df.columns if c.startswith('Q_')]]
    print(items.mean())
    print("Cronbach alpha:", cronbach_alpha(items))
