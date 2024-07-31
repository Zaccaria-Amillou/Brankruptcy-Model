import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_df_info(df):
    # Set display options for better readability
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)
    
    # Collect information in a dictionary
    info_dict = {
        "Shape": [df.shape],
        "Nb of Columns": [df.shape[1]],
        "Memory Usage (bytes)": [df.memory_usage(deep=True).sum()],
        "Number of Duplicate Rows": [df.duplicated().sum()]
    }
    
    # Create a DataFrame from the dictionary
    info_df = pd.DataFrame.from_dict(info_dict, orient='index', columns=['Details'])
    
    # Display the DataFrame
    display(info_df)
    
    # Number of unique values in each column
    unique_values = {col: df[col].nunique() for col in df.columns}
    unique_values_df = pd.DataFrame(list(unique_values.items()), columns=['Column', 'Unique Values'])
    
    # Null values in each column
    null_counts = df.isnull().sum()
    null_values_df = pd.DataFrame(null_counts, columns=['Null Values']).reset_index().rename(columns={'index': 'Column'})
    
    # Descriptive statistics
    descriptive_stats = df.describe().transpose()
    
    # Display the DataFrames
    print("\nNumber of unique values in each column:")
    display(unique_values_df)
    
    print("\nNull values in columns:")
    if null_counts.sum() == 0:
        print("There are no null values in the DataFrame.")
    else:
        display(null_values_df)
    
    print("\nDescriptive statistics of DataFrame:")
    
    return descriptive_stats
