# Comprehensive E-commerce Data Pipeline

The pipeline should combine generated sales data with data from external sources, perform data
transformations and aggregations, and store the final dataset in a database. 
The aim is to enable analysis and derive insights into customer behaviour and sales performance.

## Table of Contents
- [Introduction](#introduction)
- [Database Schema](#database-schema)
- [Reporting](#reporting-layer)

## Introduction
The goal of this project is to build an end-to-end data pipeline for e-commerce data, integrating external weather data, transforming it, and storing it in a data warehouse. Throughout the planning process, various approaches were considered to tackle emerging challenges. 
Initially, a straightforward ETL job was considered, but the project was made more challenging and modern by adopting the Medallion architecture. 
This architecture incrementally and progressively improves the structure and quality of data as it flows through each layer (from Bronze ⇒ Silver ⇒ Gold).

![arch](https://github.com/MAHMOUDMAMDOH8/E2E-e-commerce-data-pipeline/assets/111503676/f9f4f600-137f-48af-bd2b-edc2799f76cd)

### Assumptions
- The ecommerce data is assumed to be clean and does not require extensive cleaning or preprocessing.
- Weather data from the OpenWeatherMap API is assumed to be accurate and reliable.
- The database schema follows a star schema design for efficient querying and analysis.
- SCD Type 2 logic is applied to track historical changes in user and product data for analytical purposes.

### Step 1: Data Collection and Storage
We have  one Data Sources:
  -ecommerce Data: Stored in CSV format.
transform_data.py:
 -  Data is initially stored in a data lake in the "bronze" layer (raw data) in csv format to have unified landing zone.
 -  process_Ecommrese_data()
 -     - get data from bronze layear and  Removes duplicate entries and git dimensions and loade to silver layer
### Step 2: Data Delivery
 - tables_creation.py:
    - Contains functions to create, drop, and load tables, reading the statements from sql_queries.py for preparing the data warehouse.
 - load_customer_dim():
        - load transformed customer data from  silver layer, selecting required columns and loaded into a PostgreSQL database in the Gold layerles_dim()
        - Load transformed sales data from silver layer, selecting required columns and loaded into a PostgreSQL database in the Gold layer
 - load_store_dim() :
        -  load transformed customer data from  silver layer, selecting required columns and loaded into a PostgreSQL database in the Gold layerles_dim()
        -  Load transformed sales data from silver layer, selecting required columns and loaded into a PostgreSQL database in the Gold layer
 - load_product_dim():
        -  Extracts and cleans product data from the Silver layer, calculates the latest product price, and applies SCD Type 2  product
 - load_sales_fact():
        - load transformed customer data from  silver layer, selecting required columns and loaded into a PostgreSQL database in the Gold layerles_dim()
   
  db_utils.py
    - The `db_utils.py` module provides a set of database utility functions for interacting with the PostgreSQL database. 
    - These functions handle database connections, data loading, and query execution, ensuring efficient and reliable data management within the pipeline.
  
## Database Schema 
The transformed data is stored in a relational database with a star schema design, consisting of the following tables:
1. dim_customers: Contains information about users, including their name, ,segment, start date, end date, and whether they are current users.
    - Columns: customer_id, name, segment, start_date, end_date, is_current

2. fact_sales: Stores sales data along with relevant information such as product details, order quantity, price, order date, store ID, and  conditions.
    - Columns: order_id, customer_id, product_id, order_detail,quantity, SALES, order_date, store_id, Discount, PROFIT, SHIP_COST
3. dim_stores: Holds details about stores, including store ID, MARKET, REGION,COUNTRY and country.
    - Columns: store_id, MARKET, REGION, country

4. dim_product_master: Contains information about products, such as product ID, name, price, CATEGORY,SUBCATEGORY,start date, end date, and whether it is a current product.
    - Columns: product_id, product_name, CATEGORY,SUBCATEGORY,,start_date, end_date, is_current
  
![data_model](https://github.com/MAHMOUDMAMDOH8/E2E-e-commerce-data-pipeline/assets/111503676/fc4acd78-51ee-4611-a3c3-ff986004b513)

## Reporting layer


![summary](https://github.com/MAHMOUDMAMDOH8/E2E-e-commerce-data-pipeline/assets/111503676/7b1b29df-ac8a-47e8-9ce2-33c01f68c1b1)

![Orders detals](https://github.com/MAHMOUDMAMDOH8/E2E-e-commerce-data-pipeline/assets/111503676/519a7fd9-6c3a-40e4-b533-5e8c179c7416)




