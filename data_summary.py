import pandas as pd
import numpy as np

def summary_stats(df):
    return df.describe()

def most_frequent_values(df, column):
    return df[column].mode()

def unique_values(df, column):
    return df[column].unique()
