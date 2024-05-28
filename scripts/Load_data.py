from scripts.tables_creation import *
import pandas as pd
import datetime as datetime
import logging

logging.basicConfig(filename='data_delivery.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_customer_dim():
    try:
        logging.info('Loading customer_df dimension...')
        customer_df = pd.read_csv('./datalake/silver/DIM_customer.csv')
        customer_df['start_date'] = pd.to_datetime('today').date()
        customer_df['end_date'] = '2024-12-31'
        customer_df['is_current'] = True
        load_data_to_postgres('DIM_CUSTOMERS', customer_df)
        logging.info('customer_df dimension loaded successfully')
        customer_df.to_csv('./datalake/gold/customer_DIM.csv', index=False)
    except Exception as E:
        logging.error(f'Error loading users dimension: {str(E)}')

def load_store_dim():
    try:
        logging.info('Loading customer dimension...')
        store_df = pd.read_csv('./datalake/silver/DIM_store.csv')
        store_df['start_date'] = pd.to_datetime('today').date()
        store_df['end_date'] = '2024-12-31'
        store_df['is_current'] = True
        load_data_to_postgres('DIM_STORE', store_df)
        logging.info('store_df dimension loaded successfully')
        store_df.to_csv('./datalake/gold/store_dim.csv', index=False)
    except Exception as E:
        logging.error(f'Error loading users dimension: {str(E)}')

def load_product_dim():
    try:
        logging.info('Loading customer dimension...')
        product_df = pd.read_csv('./datalake/silver/DIM_product.csv')
        product_df['start_date'] = pd.to_datetime('today').date()
        product_df['end_date'] = '2024-12-31'
        product_df['is_current'] = True
        load_data_to_postgres('DIM_PRODUCT', product_df)
        logging.info('product_df dimension loaded successfully')
        product_df.to_csv('./datalake/gold/product_dim.csv', index=False)
    except Exception as E:
        logging.error(f'Error loading users dimension: {str(E)}')

def load_sales_fact():
    try:
        logging.info('Loading fact sales ...')
        sales_df = pd.read_csv('./datalake/silver/fact_sales.csv')
        load_data_to_postgres('FACT_SALES', sales_df)
        sales_df.to_csv('./datalake/gold/sales_fact.csv',index=False)
        logging.info('Sales fact loaded successfully')
    except Exception as e:
        logging.error(f'Error loading sales fact: {str(e)}')





