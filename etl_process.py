import pandas as pd
import numpy as np

# Step 1: Extract
def extract_data(file_path):
    """
    Extract data from a CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data successfully loaded from {file_path}.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Step 2: Transform
def transform_data(data):
    """
    Transform and clean the dataset.
    - Handle missing values
    - Convert date to datetime format
    - Add calculated columns like 'Daily Difference' and 'Cumulative Return'
    """
    # Drop rows with missing 'Date' or 'Name'
    data.dropna(subset=['Date', 'Name'], inplace=True)

    # Convert 'Date' to datetime format
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data.dropna(subset=['Date'], inplace=True)  # Drop invalid dates

    # Fill missing numeric values with 0
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    data[numeric_cols] = data[numeric_cols].fillna(0)

    # Calculate 'Daily Difference' (High - Low)
    if 'High' in data.columns and 'Low' in data.columns:
        data['Daily Difference'] = data['High'] - data['Low']

    # Calculate 'Cumulative Return'
    if 'Close' in data.columns:
        data['Cumulative Return'] = data['Close'].cumsum()

    print("Data transformation complete.")
    return data

# Step 3: Load
def load_data(data, output_file):
    """
    Save the cleaned and transformed data to a new CSV file.
    """
    try:
        data.to_csv(output_file, index=False)
        print(f"Data successfully saved to {output_file}.")
    except Exception as e:
        print(f"Error saving data: {e}")

# Main ETL Process
def main():
    # Input and output file paths
    input_file = "all_stocks_5_years.csv"  # Update with your file path
    output_file = "cleaned_all_stocks_5_years.csv"

    # ETL process
    print("Starting ETL process...")
    data = extract_data(input_file)
    if data is not None:
        transformed_data = transform_data(data)
        load_data(transformed_data, output_file)
    print("ETL process completed.")

if __name__ == "__main__":
    main()
