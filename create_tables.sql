CREATE OR REPLACE TABLE top_5_avg_close AS
SELECT 
    name,
    AVG(close) AS avg_close_price
FROM 
    "ETL_PIPELINE_DB"."ETL_SCHEMA"."ALL_STOCKS_5YR"
GROUP BY 
    name
ORDER BY 
    avg_close_price DESC
LIMIT 5;

CREATE OR REPLACE TABLE monthly_avg_volume AS
SELECT 
    name,
    DATE_TRUNC('month', date) AS month,
    AVG(volume) AS avg_volume
FROM 
    "ETL_PIPELINE_DB"."ETL_SCHEMA"."ALL_STOCKS_5YR"
GROUP BY 
    name, DATE_TRUNC('month', date)
ORDER BY 
    month, name;

CREATE OR REPLACE TABLE cumulative_returns AS
SELECT 
    name,
    MIN(date) AS start_date,
    MAX(date) AS end_date,
    (MAX(close) - MIN(open)) / MIN(open) * 100 AS return_percentage
FROM 
    "ETL_PIPELINE_DB"."ETL_SCHEMA"."ALL_STOCKS_5YR"
GROUP BY 
    name
ORDER BY 
    return_percentage DESC;

CREATE OR REPLACE TABLE daily_high_low_difference AS
SELECT 
    date,
    name,
    (high - low) AS daily_difference
FROM 
    "ETL_PIPELINE_DB"."ETL_SCHEMA"."ALL_STOCKS_5YR"
ORDER BY 
    date, name;

CREATE OR REPLACE TABLE top_5_volume AS
SELECT 
    name,
    SUM(volume) AS total_volume
FROM 
    "ETL_PIPELINE_DB"."ETL_SCHEMA"."ALL_STOCKS_5YR"
GROUP BY 
    name
ORDER BY 
    total_volume DESC
LIMIT 5;

CREATE OR REPLACE TABLE combined_stocks AS
SELECT 
    s.Date,
    s.Name,
    s.Close,
    s.High,
    s.Low,
    s.Volume,
    c.Cumulative_Return,
    d.Daily_Difference
FROM ALL_STOCKS_5YR s
LEFT JOIN CUMULATIVE_RETURNS c
    ON s.Date = c.Date AND s.Name = c.Name
LEFT JOIN DAILY_HIGH_LOW_DIFFERENCE d
    ON s.Date = d.Date AND s.Name = d.Name;
