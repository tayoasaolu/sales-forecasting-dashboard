# Interactive Sales Forecasting Dashboard (Power BI + SQL)

![Power BI](https://img.shields.io/badge/Power%20BI-Expert-yellow)
![SQL](https://img.shields.io/badge/SQL-Azure%20DB-blue)
![Python](https://img.shields.io/badge/Python-Automation-green)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

This project is an interactive dashboard designed to monitor Year-over-Year (YoY) sales trends, customer loyalty tiers, and inventory risks in real-time. It uses SQL for data querying, integrates with Azure SQL Database, and includes automation for daily scheduling. Built with open-source data to simulate real-world e-commerce analytics.

The dashboard helps businesses forecast sales, identify loyal customers, and mitigate inventory issues, providing actionable insights for decision-making.

## Features
- **YoY Trends**: Visualize sales growth over time with line charts and growth percentages.
- **Customer Loyalty Tiers**: Segment customers into tiers (e.g., High, Medium, Low) based on purchase frequency.
- **Inventory Risks**: Real-time alerts for low-stock or overstock items to prevent losses.
- **Automation**: Daily scheduled queries using Python, integrated with Azure DB for seamless updates.
- **Interactivity**: Slicers, drill-downs, and filters in Power BI for dynamic exploration.

## Dataset
This project uses the open-source [Superstore Sales Dataset from Kaggle](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting). 
- **Why this dataset?** It includes sales transactions with dates, customer details, products, quantities, and profits—perfect for YoY analysis, loyalty segmentation, and inventory tracking.
- **License**: CC0 (Public Domain). Download the CSV and place it in the `data/` folder.

## Technologies Used
- **Power BI**: For building the interactive dashboard.
- **SQL**: Querying and transforming data (compatible with Azure SQL Database).
- **Python**: Automation and scheduling (libraries: pandas, sqlalchemy, schedule).
- **Azure SQL Database**: For data storage and integration (free tier used for development).
- **Other Tools**: Git for version control.

## Setup Instructions
1. **Clone the Repository**:
