import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    # Drop duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.fillna(method='ffill')
    
    # Convert date columns
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    
    return df
