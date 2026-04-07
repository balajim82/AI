"""
 This file we are going discuss about the pandas library in python.

1. What is pandas?
    -- pandas is a powerful and flexible open-source data analysis and manipulation library for Python.
       It provides data structures and functions needed to work with structured data seamlessly.
       The name "pandas" is derived from "panel data," which refers to multidimensional data sets.
    > Fast and efficient DataFrame object
    > Tools for reading/writing data
    >Data cleaning and preparation
    > Data analysis and visualization integration
2. Why use pandas?
    -- pandas is widely used in data analysis, data science, and machine learning due to its versatility and ease of use.
      It allows you to handle and analyze data efficiently, making it a go-to choice for data manipulation tasks.
    With pandas, you can easily perform operations like filtering, grouping, and aggregating data, which are essential for data analysis.

3. Table of Contents:
    Introduction to Pandas
    Pandas Data Structures
    Creating DataFrames
    Reading and Writing Data
    Data Inspection
    Data Selection and Indexing
    Data Cleaning
    Data Manipulation
    Grouping and Aggregation
    Merging, Joining, and Concatenating

Key Points:
In Pandas- Series (Column) and DataFrame (Data Table) are the two primary data structures used for data manipulation and analysis.
Internally pandas uses NumPy arrays to store data, which allows for efficient memory usage and fast computations.

"""

# Series  cretion from List and assign index
# Series (1-Dimensional)

import pandas as pd
import numpy as np

data = [10, "balaji", 30, 40, 50]
index = ["A", "B", "C", "D", "E"]
pd_series = pd.Series(data)  # without index, auto-generated index will be created
print(pd_series, type(pd_series))

pd_series_with_index = pd.Series(data, index=index)  # with index
print(pd_series_with_index, type(pd_series_with_index))

# Serious generation dynamically from list comprehension
dynamic_series = pd.Series(
    [i * 1 for i in range(6)], index=["A", "B", "C", "D", "E", "F"]
)
print(dynamic_series, type(dynamic_series))

# Dynamic series and index generation using list comprehension
dynamic_series_index = pd.Series(
    [i * 2 for i in range(6)], index=[f"{i}" for i in range(6)]
)
print(dynamic_series_index, type(dynamic_series_index))

# series and inderx headers
dynamic_series_index = pd.Series(
    [i * 2 for i in range(6)], index=[f"{i}" for i in range(6)], name="Sales_Data"
)
print(dynamic_series_index.to_frame(), type(dynamic_series_index))

# series creation from scalar value
scalar_series = pd.Series(100, index=["A", "B", "C", "D", "E"])
print(scalar_series, type(scalar_series))

# Series creation from dictionary
data_dict = {"A": 10, "B": 20, "C": 30, "D": 40, "E": 50}
series_from_dict = pd.Series(data_dict)
print(series_from_dict, type(series_from_dict))


# Series creation from dictionary with headers
data_dict = {"A": 10, "B": 20, "C": 30, "D": 40, "E": 50}
series_from_dict_with_name = pd.Series(data_dict, name="Sales_Data")
print(series_from_dict_with_name.to_frame(), type(series_from_dict_with_name))

# Accessing Series elements using index labels
print(series_from_dict_with_name["A"])  # Accessing element with index label 'A'
print(series_from_dict_with_name[:3])  # Accessing element with integer position 0 to 2

# Series Attributes
print(series_from_dict_with_name.index)  # Index labels
print(series_from_dict_with_name.values)  # Series values
print(series_from_dict_with_name.dtype)  # Data type of the Series
print(series_from_dict_with_name.name)  # Name of the Series


# 2.2 DataFrame (2-Dimensional)
# DataFrame creation from dictionary of lists and should same lenght of list
data_dict = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}
df = pd.DataFrame(data_dict)
print(df["Age"].sum())  # Sum of the "Age" column

# DataFrame Attributes
# Key attributes
print(f"Shape (rows, cols): {df.shape}")
print(f"Columns: {df.columns}")
print(f"Index: {df.index}")
print(f"Data types:\n{df.dtypes}")
print(f"Size (total elements): {df.size}")


# Section 3: Creating DataFrames
# 3.1 From Dictionary of Lists
data_dict = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}
df_from_dict = pd.DataFrame(data_dict)
print(df_from_dict)

# Method 1: value of Dictionary is lists
data_dict = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}
df_from_dict = pd.DataFrame(data_dict)
print(df_from_dict)

## Method 2: List of dictionaries

data_list_of_dicts = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"},
    {"Name": "David", "Age": 40, "City": "Houston"},
]

df_from_list_of_dicts = pd.DataFrame(data_list_of_dicts)
print(df_from_list_of_dicts)


# 3.2 From Lists and Arrays
# From 2D list
data = [
    ["Product A", 100, "Electronics"],
    ["Product B", 50, "Books"],
    ["Product C", 75, "Clothing"],
]
df3 = pd.DataFrame(data, columns=["Product", "Price", "Category"])
print(df3)

## From NumPy array
arr = np.random.randint(0, 100, size=(5, 3))
df4 = pd.DataFrame(arr, columns=["Col1", "Col2", "Col3"])
print(f"\nFrom NumPy array:\n{df4}")

# 3.3 From Series
# Combine multiple Series
names = pd.Series(["John", "Jane", "Mike"])
ages = pd.Series([28, 34, 29])
cities = pd.Series(["NYC", "LA", "Chicago"])

df5 = pd.DataFrame({"Name": names, "Age": ages, "City": cities})
print(df5)

# Section 4: Reading and Writing Data
# various ways retriveing data from diff source
# 1. From CSV file
# 2. From Excel file
# 3. From SQL database
# 4. From JSON file
# 5. From HTML tables
# 6. From clipboard
# 7. From API
# 8. Manual data frame creation using dictionaries, lists, or arrays

# 3.4 Sample Datasets for Practice
# Create sample sales dataset
np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=100, freq="D")
sales_data = {
    "Date": dates,
    "Product": np.random.choice(["A", "B", "C", "D"], 100),
    "Region": np.random.choice(["North", "South", "East", "West"], 100),
    "Sales": np.random.randint(100, 1000, 100),
    "Quantity": np.random.randint(1, 20, 100),
    "Customer_Type": np.random.choice(["New", "Returning"], 100),
}
sales_df = pd.DataFrame(sales_data)
print(sales_df.head())  # Head means first 5 rows of the data frame
print(sales_df.tail())  # Tail means last 5 rows of the data framecls


# Read CSV
# df = pd.read_csv('data.csv')

# With parameters
# df = pd.read_csv('data.csv',
#                  sep=',',           # Delimiter
#                  header=0,          # Row number for column names
#                  index_col=0,       # Column to use as index
#                  usecols=['A', 'B'], # Specific columns to read
#                  nrows=1000,        # Number of rows to read
#                  skiprows=5,        # Rows to skip
#                  na_values=['NA', 'NULL'])  # Values to treat as NaN

# For demonstration, create and read CSV
# sales_df.to_csv(
#     "D:/Ai-Programs/GIT_CODE_PYTHON/python_pandas_numpy_concepts/products_2026-03-20_18-14-25_1.csv",
#     index=False,
# )
path = "D:/Ai-Programs/GIT_CODE_PYTHON/python_pandas_numpy_concepts/import_inv/products_2026-03-20_18-14-25_1.csv"

pd_read_csv = pd.read_csv(path, index_col=0)
print(pd_read_csv.head())

path_excel = "D:/Ai-Programs/GIT_CODE_PYTHON/python_pandas_numpy_concepts/import_inv/Home-Painting.xlsx"
# Read Excel
df = pd.read_excel(path_excel,sheet_name='Sheet1')
print(df.head())
# Multiple sheets
df_dict = pd.read_excel(path_excel, sheet_name=None)  # All sheets
print(df_dict.keys())  # Print sheet names
print(df_dict['Sheet1'].head())  # Access specific sheet



# Read JSON
# Create sample JSON
 
path_json = "D:/Ai-Programs/GIT_CODE_PYTHON/python_pandas_numpy_concepts/import_inv/sample_data_json.json"

df_json = pd.read_json(path_json)
print(f"\nFrom JSON:\n{df_json}")

# Along with above reading techniques from HTML, DataBase or API. 
# For getting data from any source, we can manipulate data. Like
#  1. Data Cleaning (Handling missing values, duplicates, data types)
#  2. Data Transformation (Sorting, filtering, grouping)
#  3. Data Analysis (Descriptive statistics, correlation, visualization)
  
