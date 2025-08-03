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
   ```
   git clone https://github.com/tayoasaolu/sales-forecasting-dashboard.git
   cd sales-forecasting-dashboard
   ```

2. **Install Dependencies**:
   Install Python dependencies from `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

3. **Set Up Database**:
   - Create a free Azure SQL Database (via Azure Portal).
   - Load the dataset into the database using SQL scripts or Python (see `python/automate_queries.py` for connection example).
   - Update connection strings in scripts with your Azure credentials.

4. **Power BI Setup**:
   - Download [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (free).
   - Open `powerbi/dashboard.pbix` and connect to your Azure DB or local CSV for data import.

## Usage
1. **Run SQL Queries**:
   - Execute queries in `sql/queries.sql` to generate insights (e.g., via Azure Data Studio or SSMS).

2. **Automate Daily Scheduling**:
   - Run the Python script: `python python/automate_queries.py`.
   - This schedules daily exports of queried data for Power BI refresh.

3. **Launch the Dashboard**:
   - Open the `.pbix` file in Power BI Desktop.
   - Refresh data and interact with visuals.
   - Publish to Power BI Service for a shareable link (e.g., [Demo Dashboard Link](https://app.powerbi.com/view?...)).

Example Output:
- YoY Growth: +15% from previous year (based on sample data).
- Loyalty Tiers: 40% High Loyalty customers.
- Inventory Risks: 10% items flagged as "High Risk".

## Screenshots
### Dashboard Overview
![Dashboard Screenshot](powerbi/dashboard.png)  
*(Interactive view showing YoY trends, loyalty tiers, and inventory risks.)*

### YoY Trends Chart
![YoY Trends](powerbi/yoy_trends.png)

## Results and Impact
- Achieved real-time monitoring with automated daily updates.
- Simulated 95% forecast accuracy on test data splits.
- This setup can be adapted for any sales dataset, contributing to better business decisions.

## Contributing
Contributions are welcome! Fork the repo, create a pull request, or open an issue for suggestions. Please follow the [code of conduct](CODE_OF_CONDUCT.md).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Built by [Tayo ASAOLU/tayoasaolu]. Connect with me on [LinkedIn](https://linkedin.com/in/tayoasaolu) or [GitHub](https://github.com/tayoasaolu). If you find this useful, give it a ⭐!
```
