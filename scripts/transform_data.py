import pandas as pd
import datetime as datetime
import logging
import os

def process_Ecommrese_data():
    df = pd.read_excel('./datalake/bronze/E-commerce.xlsx')
    df.rename(columns={'Row ID': 'order_id', 'Order ID': 'order_detail', 'LOC ID': 'STORE_ID'}, inplace=True)
    df.drop_duplicates(subset=['order_id'], inplace=True)
    df = df[['order_id', 'order_detail', 'Order Date', 'Customer ID', 'Customer Name', 'Segment',
             'STORE_ID', 'Market', 'Region', 'Country', 'Product ID', 'Product Name', 'Sub-Category',
             'Category', 'Sales', 'Quantity', 'Discount', 'Profit', 'Shipping Cost']]

    store = df[['STORE_ID', 'Market', 'Region', 'Country']].drop_duplicates(subset=['STORE_ID'])
    store = store.rename(columns={'STORE_ID':'store_id','Market':'market','Region':'region','Country':'country'})

    customer = df[['Customer ID', 'Customer Name', 'Segment']].drop_duplicates(subset=['Customer ID'])
    customer = customer.rename(columns={'Customer ID':'customer_id', 'Customer Name':'name', 'Segment':'segment'})


    product = df[['Product ID', 'Product Name', 'Sub-Category', 'Category']].drop_duplicates(subset=['Product ID'])
    product = product.rename(columns={'Product ID':'product_id', 'Product Name':'name', 'Sub-Category':'subcategory', 'Category':'category'})


    fact_sales = df[['order_id','order_detail','Customer ID', 'Product ID','STORE_ID','Order Date','Sales','Quantity','Discount','Profit','Shipping Cost']]
    fact_sales = fact_sales.rename(columns={
        'Customer ID':'customer_id', 'Product ID':'product_id','STORE_ID':'store_id',
        'Order Date':'Order_Date','Sales':'sales','Quantity':'quantity',
        'Discount':'discount','Profit':'profit','Shipping Cost':'ship_cost'
    })

    store.to_csv('/opt/airflow/datalake/silver/DIM_store.csv', index=False)
    customer.to_csv('/opt/airflow/datalake/silver/DIM_customer.csv', index=False)
    product.to_csv('/opt/airflow/datalake/silver/DIM_product.csv', index=False)
    fact_sales.to_csv('/opt/airflow/datalake/silver/fact_sales.csv', index=False)
    logging.info('ecommerce data processing completed')

