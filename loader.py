"""
LOADER.PY

If it's possible, loads the csv file and save it into a returnable variable called csv.
"""

import pandas as pd
import os

def load(file):
    try:
        csv = pd.read_csv(file)
        df_name = os.path.splitext(os.path.basename(file))[0]
        print("CSV successfully loaded.\n\n")
    except FileNotFoundError:
        raise FileNotFoundError("File couldn't be loaded. Please verify file's name and path.\n")
    
    return csv, df_name