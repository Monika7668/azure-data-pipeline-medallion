# Architecture Diagram

## Flow:
ADF → Data Lake (Bronze)
        ↓
Databricks (Silver - Cleaning)
        ↓
Delta Lake (Gold - Aggregation)
        ↓
SQL / BI Tools

## Description:
- Bronze layer stores raw data
- Silver layer applies cleaning & validation
- Gold layer provides business insights
