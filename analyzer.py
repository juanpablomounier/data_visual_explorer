"""
ANALYZER.PY

Analyzes a few elements of the dataframe and save them into returnable variables for showing purposes.
"""

import pandas as pd

def analyze(df):
    df_shape = df.shape
    df_num_valid_columns = df.select_dtypes(include=["number"])
    invalid_columns = []
    for column in df_num_valid_columns:
        if "id" in column:
            invalid_columns.append(column)
    df_num_valid_columns = df_num_valid_columns.drop(columns=invalid_columns, errors='ignore')
    corr_matrix = df_num_valid_columns.corr()

    return df_shape, df_num_valid_columns, corr_matrix

