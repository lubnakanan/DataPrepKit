import pandas as pd

def remove_missing(df):
    return df.dropna()

def impute_missing(df, strategy='mean'):
    if strategy == 'mean':
        return df.fillna(df.mean())
    elif strategy == 'median':
        return df.fillna(df.median())
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    else:
        raise ValueError("Invalid imputation strategy")

def missing_value_stats(df):
    return df.isnull().sum()
