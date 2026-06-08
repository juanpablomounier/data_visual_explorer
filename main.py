"""
MAIN.PY

Orchestrates the pipeline. It call all the methods in order to load, analyze and show data.
"""

from loader import load
from analyzer import analyze
from visualizer import visualize

print("*"*34)
print("WELCOME TO DATASET_VISUAL_EXPLORER")
print("*"*34)
print("\n")


file = "datasets/employee_analytics_dataset.csv"
df, df_name = load(file)
shape, numeric_columns, corr_matrix = analyze(df)
visualize(df, df_name, shape, numeric_columns, corr_matrix)
