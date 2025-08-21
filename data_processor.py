import pandas as pd

def get_high_value_customers(filepath):
    df = pd.read_csv(filepath)
    return df[df['Rating'] > 4]

def calculate_total_visits(df):
    total = df['Visits'].iloc[:-1].sum()
    return total
