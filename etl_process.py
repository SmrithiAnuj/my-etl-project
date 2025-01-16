import pandas as pd
import numpy as np

# Function to load data from a CSV file
def extract_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from: {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to clean and transform the dataset
def transform_data(data):
    # Remove rows with missing 'Date' or 'Name'
    data.dropna(subset=['Date', 'Name'], inplace=True)

    # Convert 'Date' to datetime format and remove invalid entries
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data.dropna(subset=['Date'], inplace=True)

    # Fill missing numeric values with 0
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    data[numeric_cols] = data[numeric_cols].fillna(0)

    # Add calculated columns
    if 'High' in data.columns and 'Low' in data.columns:
        data['Daily Difference'] = data['High'] - data['Low']
    if 'Close' in data.columns:
        data['Cumulative Return'] = data['Close'].cumsum()

    print("Data transformation complete.")
    return data

# Function to save the cleaned data to a new CSV file
def load_data(data, output_file):
    try:
        data.to_csv(output_file, index=False)
        print(f"Data saved to: {output_file}")
    except Exception as e:
        print(f"Error saving data: {e}")

# Main function to execute the ETL process
def main():
    input_file = "all_stocks_5_years.csv"  # Input file path
    output_file = "cleaned_all_stocks_5_years.csv"  # Output file path

    print("Starting ETL process...")
    data = extract_data(input_file)
    if data is not None:
        transformed_data = transform_data(data)
        load_data(transformed_data, output_file)
    print("ETL process completed.")

if __name__ == "__main__":
    main()

