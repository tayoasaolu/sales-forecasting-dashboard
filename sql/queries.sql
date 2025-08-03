-- queries.sql
-- This file contains SQL queries for the Interactive Sales Forecasting Dashboard.
-- Assumes the table name is 'superstore_sales' from the Kaggle Superstore Dataset.
-- Columns used: OrderDate (datetime), Sales (float), CustomerID (varchar), OrderID (varchar), ProductID (varchar), Quantity (int).
-- Run these in Azure SQL Database or any SQL-compatible DB.

-- 1. YoY Sales Trends
-- Calculates total sales per year, previous year's sales, and YoY growth percentage.
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

-- 2. Customer Loyalty Tiers
-- Segments customers based on purchase count: High (>10), Medium (5-10), Low (<5).
-- Adjust thresholds as needed for your analysis.
SELECT 
    CustomerID,
    COUNT(OrderID) AS PurchaseCount,
    CASE 
        WHEN COUNT(OrderID) > 10 THEN 'High Loyalty'
        WHEN COUNT(OrderID) BETWEEN 5 AND 10 THEN 'Medium Loyalty'
        ELSE 'Low Loyalty'
    END AS LoyaltyTier
FROM superstore_sales
GROUP BY CustomerID
ORDER BY PurchaseCount DESC;

-- 3. Inventory Risks
-- Flags products based on total quantity: High Risk (<10), Medium Risk (>100 overstock), Low Risk (others).
-- Assumes 'Quantity' represents stock levels; adapt if using actual inventory data.
SELECT 
    ProductID,
    SUM(Quantity) AS TotalStock,
    CASE 
        WHEN SUM(Quantity) < 10 THEN 'High Risk (Low Stock)'
        WHEN SUM(Quantity) > 100 THEN 'Medium Risk (Overstock)'
        ELSE 'Low Risk'
    END AS InventoryRisk
FROM superstore_sales
GROUP BY ProductID
ORDER BY TotalStock ASC;

-- Additional Query: Sample Data Preview (for testing)
SELECT TOP 10 * FROM superstore_sales;
