import pandas as pd
import numpy as np

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    df_copy = df.copy()
    df_copy = df_copy.drop(columns=['CUST_ID', 'PURCHASES_INSTALLMENTS_FREQUENCY', 'ONEOFF_PURCHASES', 'CASH_ADVANCE_FREQUENCY'])
    df_copy = df_copy.dropna()
    return df_copy

def apply_log_transformation(df, skewness_features):
    df[skewness_features] = np.log(df[skewness_features] + 0.1)
    return df
