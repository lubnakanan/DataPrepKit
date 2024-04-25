import pandas as pd

def label_encoding(df, column):
    df[column] = df[column].astype('category')
    df[column + '_encoded'] = df[column].cat.codes
    return df

def one_hot_encoding(df, column):
    return pd.get_dummies(df, columns=[column], prefix=[column])

def ordinal_encoding(df, column, mapping):
    df[column] = df[column].map(mapping)
    return df
