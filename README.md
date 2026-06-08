## Welcome to DATASET_VISUAL_EXPLORER

This application loads a CSV dataset, analyzes the data and provides a quick overview including:

- Detect numeric columns
- Generate histograms
- Generate visual reports

## Structure

DATASET_VISUAL_EXPLORER/
│
├── datasets/
│   └── CSV files
├── outputs/
│   └── Figure files
│
├── main.py
│   └── Orchestrates the application workflow
│
├── loader.py
│   └── Loads and validates CSV datasets
│
├── analyzer.py
│   └── Performs data analysis and generates statistics
│
└── visualizer.py
    └── Displays summarized results and insights

## Installation

pip install -r requirements.txt



## Usage

python main.py



## An example of the output:

**********************************
WELCOME TO DATASET_VISUAL_EXPLORER
**********************************

CSV successfully loaded.

The dataframe's shape is: 
 Rows: 30
 Columns: 7

-------------------------

Numeric columns are: 

employee_id
age
salary_usd
years_experience
performance_score

-------------------------

Analyzing and creating figures...

(Output truncated for brevity)

## Features

- Load CSV datasets
- Automatically detect numeric columns
- Ignore identifier columns (e.g. employee_id)
- Generate histograms for numeric variables
- Generate a correlation matrix
- Save visualizations as image files
- Organize outputs automatically

## Author

Juan Pablo Mounier

Github: https://github.com/juanpablomounier