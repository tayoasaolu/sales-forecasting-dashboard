# Dataset Information and Download Instructions

## Overview
This project uses the [Superstore Sales Dataset from Kaggle](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting) for all analysis. It contains ~10,000 rows of sales data, including columns like `OrderDate`, `Sales`, `CustomerID`, `OrderID`, `ProductID`, `Quantity`, and more.

- **Why this dataset?** It's open-source, well-structured, and ideal for demonstrating YoY trends, customer loyalty, and inventory risks without using proprietary data.
- **License**: CC0 (Public Domain) – free to use and modify.
- **File Format**: CSV (train.csv or similar; rename to superstore_sales.csv for consistency).

Do **not** upload the full dataset to this repo to avoid bloat. Instead, follow the steps below to download and prepare it locally.

## Download Steps
1. **Go to Kaggle**: Visit the [dataset page](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting).
2. **Sign In/Register**: Create a free Kaggle account if you don't have one.
3. **Download**: Click "Download" to get the ZIP file. Extract the CSV (e.g., `train.csv`).
4. **Rename and Place**: Rename the file to `superstore_sales.csv` and place it in this `data/` folder locally for reference.

## Loading into Database
To use with SQL queries and automation:
- **Option 1: Local Testing (SQLite)**:
  - Install SQLite (free) and use a tool like DB Browser for SQLite.
  - Import the CSV into a table named `superstore_sales`.

- **Option 2: Azure SQL Database (Recommended)**:
  1. Create a free Azure account and set up an Azure SQL Database via the Azure Portal.
  2. Use Azure Data Studio or SSMS to connect.
  3. Create a table:
     ```sql
     CREATE TABLE superstore_sales (
         OrderDate DATETIME,
         Sales FLOAT,
         CustomerID VARCHAR(50),
         OrderID VARCHAR(50),
         ProductID VARCHAR(50),
         Quantity INT
         -- Add more columns as per the dataset
     );
     ```
  4. Import the CSV using Azure's import tools or a script (e.g., via Python with pandas and sqlalchemy).

## Exported Files
- The automation script (`../python/automate_queries.py`) will generate CSVs here, like `yoy_trends.csv`, after running queries.
- These can be directly imported into Power BI for the dashboard.

If you encounter issues with data types or columns, refer to the Kaggle dataset description for full schema details.
