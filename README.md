# My ETL Project with Tableau Dashboard

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for processing stock market data. The project involves:
- Extracting and transforming raw data using Python.
- Loading the data into Snowflake for analysis.
- Visualizing insights using a Tableau dashboard.
## Project Structure
/my-etl-project ├── /etl │ ├── etl_process.py # Python script for ETL process ├── /snowflake │ ├── create_tables.sql # SQL script to create tables │ ├── data_modeling.sql # SQL script for data modeling ├── /data │ ├── all_stocks_5_years.csv.zip # Compressed dataset used for the pipeline ├── /dashboard │ ├── dashboard_screenshot.png # Screenshot of the Tableau dashboard │ ├── tableau_dashboard_link.txt # Link to the live Tableau dashboard ├── README.md # Project documentation

## How to Run the Project
Follow these steps to set up and run the project:

### Step 1: Set Up the Environment
1. Install Python 3.x and the required libraries:
   ```bash
   pip install pandas numpy

### Step 2: Execute the ETL Pipeline
1. Extract and Transform Data:

Run the Python script located in the /etl folder:
bash
Copy code
python etl/etl_process.py
This will process the raw dataset and create a cleaned dataset in the /data folder

2. Load Data into Snowflake:

Execute the SQL scripts in the /snowflake folder in the following order:
create_tables.sql: Creates necessary tables.
data_modeling.sql: Models the data for analysis.

### Step 3: Visualize Insights in Tableau
Import the processed data into Tableau.
Open the Tableau dashboard

### Dashboard Overview
The Tableau dashboard provides:

Monthly average stock volumes.
Top 5 stocks with the highest cumulative returns.
Daily high-low differences for better insights.

### Dashboard Overview
The Tableau dashboard provides:

Monthly average stock volumes.
Top 5 stocks with the highest cumulative returns.
Daily high-low differences for better insights.

### Acknowledgments
Snowflake for providing a powerful cloud-based database solution.
Tableau for enabling easy and interactive visualizations.
Pandas and NumPy libraries for efficient data manipulation.
