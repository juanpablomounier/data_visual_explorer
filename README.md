## Welcome to DATASET_TERMINAL

This application loads CSV datasets and provides a quick overview including:

- Dataset dimensions
- Column names
- Data types
- Missing values
- Descriptive statistics



## Structure

DATASET_TERMINAL/
│
├── datasets/
│   └── CSV files
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

***************************
WELCOME TO DATASET_TERMINAL
***************************

CSV successfully loaded.

Rows: 2000
Columns: 24

Missing values:

brand        0
model        0
price_usd    0

...

(Output truncated for brevity)

## Features

- Load CSV datasets
- Inspect dataset dimensions
- Display column names
- Detect data types
- Count missing values
- Generate descriptive statistics


## Author

Juan Pablo Mounier

Github: https://github.com/juanpablomounier