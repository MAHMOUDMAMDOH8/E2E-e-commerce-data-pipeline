from scripts.SQL.SQL_QUERY import *
from scripts.Utils.db_utils import *

logging.basicConfig(filename='tables_creation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_tables(host,db_name,user,password):

    logging.info('create tables ..... ')
    queries =[
        (CREATE_CUSTOMER_TABLE_SQL, 'CUSTOMER'),
        (CREATE_PRODUCT_TABLE_SQL, 'PRODUCT'),
        (CREATE_STORE_TABLE_SQL, 'STORE'),
        (CREATE_FACTSALES_TABLE_SQL, 'FACTSALES')
    ]
    conn = create_connection(host,db_name,user,password)
    if conn:
        cursor = conn.cursor()
        for query,table in queries:
            if execute_query(conn, query, table):
                logging.info(f'Table {table} created successfully')
            else:
                logging.error(f'Failed to create table {table}')
    else:
        logging.error('Failed to establish a connection to the database')
def drop_tables(host,db_name,user,password):

    logging.info('Dropping tables...')
    queries = [
        (drop_CUSTOMER_TABLE_SQL, 'CUSTOMER'),
        (drop_PRODUCT_TABLE_SQL, 'PRODUCT'),
        (drop_STORE_TABLE_SQL, 'STORE'),
        (drop_FACTSALES_TABLE_SQL, 'FACTSALES')
    ]
    conn = create_connection(host,db_name,user,password)
    if conn:
        cursor = conn.cursor()
        for query, table_name in queries:
            if execute_query(conn, query, table_name):
                logging.info(f'Table {table_name} dropped successfully')
            else:
                logging.error(f'Failed to drop table {table_name}')
        close_connection(conn)
    else:
        logging.error('Failed to establish a connection to the database')
def load_data_to_postgres(table_name, data_frame,host,db_name,user,password):

    logging.info(f'Loading data into table {table_name}...')
    conn = create_connection(host,db_name,user,password)
    if conn:
        cursor = conn.cursor()
        cursor.execute(f"TRUNCATE TABLE {table_name} RESTART IDENTITY;")
        # Insert new data
        for i, row in data_frame.iterrows():
            cols = ', '.join(list(row.index))
            vals = ', '.join(['%s'] * len(row))
            insert_query = f"INSERT INTO {table_name} ({cols}) VALUES ({vals})"
            cursor.execute(insert_query, tuple(row))
        conn.commit()
        logging.info(f"Data loaded successfully into table {table_name}")
        close_connection(conn)
    else:
        logging.error(f"Failed to connect to the database and load data into table {table_name}")