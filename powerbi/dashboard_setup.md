# Power BI Dashboard Setup Instructions

## Overview
This file guides you through building the Interactive Sales Forecasting Dashboard in Power BI Desktop. The dashboard visualizes YoY trends, customer loyalty tiers, and inventory risks using data from the Superstore Sales Dataset (see `../data/download_dataset.md`).

- **Prerequisites**:
  - [Power BI Desktop](https://powerbi.microsoft.com/desktop/) installed (free).
  - Dataset loaded into Azure SQL Database or available as CSV (e.g., `superstore_sales.csv` or exported CSVs like `yoy_trends.csv` from automation).
  - SQL queries from `../sql/queries.sql` executed and ready for import.

If you have the pre-built `dashboard.pbix` file (uploaded to this folder), simply open it in Power BI Desktop and refresh the data. Otherwise, follow the steps below to build it from scratch.

## Step 1: Import Data
1. Open Power BI Desktop and create a new report.
2. Click **Get Data** > **SQL Server** (for Azure DB) or **Text/CSV** (for local files).
   - For Azure: Enter your server details (e.g., `your_server.database.windows.net`) and credentials. Select the `superstore_sales` table or run queries directly.
   - For CSV: Import files like `../data/yoy_trends.csv`, `../data/loyalty_tiers.csv` (generate via automation script if needed).
3. Load the data. If using queries, use **Get Data > Blank Query** and paste SQL (e.g., the YoY query) into the Advanced Editor.

## Step 2: Create DAX Measures
In the **Fields** pane, create new measures for calculations (right-click > New Measure). Examples:

- **Total Sales**:
  ```
  Total Sales = SUM(superstore_sales[Sales])
  ```

- **YoY Growth %** (based on SQL query output or calculated in DAX):
  ```
  YoY Growth % = 
  VAR CurrentYearSales = [Total Sales]
  VAR PreviousYearSales = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
  RETURN
  IF(NOT ISBLANK(PreviousYearSales), DIVIDE(CurrentYearSales - PreviousYearSales, PreviousYearSales), BLANK())
  ```

- **Loyalty Tier Count** (for summarizing tiers):
  ```
  High Loyalty Count = COUNTROWS(FILTER(superstore_sales, [LoyaltyTier] = "High Loyalty"))
  ```

- **Inventory Risk Alert**:
  ```
  High Risk Items = COUNTROWS(FILTER(superstore_sales, [InventoryRisk] = "High Risk (Low Stock)"))
  ```

(Adapt these based on your data model. Create a Date table if needed for time intelligence: Modeling > New Table > `Date = CALENDARAUTO()`.)

## Step 3: Build Visuals
1. **YoY Trends**: Add a Line Chart. Drag `Year` to Axis, `Total Sales` to Values, and `YoY Growth %` as a secondary line.
2. **Customer Loyalty Tiers**: Add a Pie or Bar Chart. Drag `LoyaltyTier` to Legend, `PurchaseCount` to Values.
3. **Inventory Risks**: Add a Card or Gauge Visual. Use `High Risk Items` for values, add conditional formatting for alerts (e.g., red for high risk).
4. **Interactivity**: Add Slicers (e.g., for `Year` or `ProductID`). Enable drill-down on charts.

## Step 4: Add Interactivity and Automation
- **Filters/Slicers**: Add date range slicers for real-time filtering.
- **Refresh Scheduling**: In Power BI Service (after publishing), set up scheduled refresh connected to Azure DB.
- **Publish**: File > Publish to Power BI Service. Share a public link in the README.

## Testing and Tips
- Refresh the data to see updates from automated queries.
- Test with sample data: Expect ~15% YoY growth and balanced loyalty tiers based on the dataset.
- Performance: If slow, optimize by importing only necessary columns.
- Export as PDF or embed in web for sharing.

## Screenshots and Files
- Upload screenshots here (e.g., `dashboard.png`) after building.
- If uploading the `.pbix` file: Add `dashboard.pbix` to this folder (keep under 100 MB).

For issues, refer to [Power BI Documentation](https://docs.microsoft.com/power-bi/) or open a GitHub issue.
