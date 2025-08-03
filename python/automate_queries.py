# automate_queries.py
# This script automates running SQL queries from the database and exporting results to CSV.
# It integrates with Azure SQL Database and schedules daily runs (e.g., at 8 AM).
# Dependencies: pandas, sqlalchemy, pyodbc, schedule (install via requirements.txt).
# Update the connection string with your Azure credentials.

import pandas as pd
import sqlalchemy as sa
import schedule
import time
import logging  # For basic error logging

# Set up logging for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Azure SQL Database connection string
# Replace with your actual details: server name, database name, username, password.
# Example: 'mssql+pyodbc://username:password@server.database.windows.net/dbname?driver=ODBC+Driver+17+for+SQL+Server'
connection_string = 'mssql+pyodbc://your_username:your_password@your_server.database.windows.net/your_dbname?driver=ODBC+Driver+17+for+SQL+Server'
engine = sa.create_engine(connection_string)

def run_queries():
    try:
        # Example: Run YoY Trends query (paste or reference from sql/queries.sql)
        query_yoy = """
        SELECT 
            YEAR(OrderDate) AS Year,
            SUM(Sales) AS TotalSales,
            LAG(SUM(Sales)) OVER (ORDER BY YEAR(OrderDate)) AS PreviousYearSales,
            CASE 
                WHEN LAG(SUM(Sales)) OVER (ORDER BY YEAR(OrderDate)) IS NOT NULL 
                THEN (SUM(Sales) - LAG(SUM(Sales)) OVER (ORDER BY YEAR(OrderDate))) / LAG(SUM(Sales)) OVER (ORDER BY YEAR(OrderDate)) * 100 
                ELSE NULL 
            END AS YoY_Growth_Percent
        FROM superstore_sales
        GROUP BY YEAR(OrderDate)
        ORDER BY Year;
        """
        
        # Execute query and load into DataFrame
        df_yoy = pd.read_sql(query_yoy, engine)
        
        # Export to CSV for Power BI import
        df_yoy.to_csv('data/yoy_trends.csv', index=False)
        logging.info("YoY trends query executed and exported to data/yoy_trends.csv")
        
        # Add more queries here (e.g., loyalty tiers, inventory risks) similarly.
        # Example:
        # query_loyalty = "YOUR_LOYALTY_QUERY_HERE"
        # df_loyalty = pd.read_sql(query_loyalty, engine)
        # df_loyalty.to_csv('data/loyalty_tiers.csv', index=False)
        
    except Exception as e:
        logging.error(f"Error running queries: {e}")

# Schedule the task to run daily at 8:00 AM
schedule.every().day.at("08:00").do(run_queries)

# Main loop to keep the script running and check for scheduled tasks
if __name__ == "__main__":
    logging.info("Automation script started. Waiting for scheduled tasks...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
