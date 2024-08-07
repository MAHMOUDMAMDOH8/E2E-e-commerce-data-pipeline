CREATE_CUSTOMER_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS DIM_CUSTOMERS(
     CUSTOMER_ID VARCHAR(225) PRIMARY KEY ,
     name VARCHAR(225),
     SEGMENT VARCHAR(225),
     start_date DATE,
     end_date DATE,
     is_current BOOLEAN
)
"""

CREATE_PRODUCT_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS DIM_PRODUCT(
     PRODUCT_ID VARCHAR(225) PRIMARY KEY ,
     name VARCHAR(225),
     SUBCATEGORY VARCHAR(225),
     CATEGORY VARCHAR(225),
     start_date DATE,
     end_date DATE,
     is_current BOOLEAN
)
"""

CREATE_STORE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS DIM_STORE(
     STORE_ID VARCHAR(225) PRIMARY KEY ,
     MARKET VARCHAR(10),
     REGION VARCHAR(20),
     COUNTRY VARCHAR(50),
     start_date DATE,
     end_date DATE,
     is_current BOOLEAN
)
"""

CREATE_FACTSALES_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS FACT_SALES(
     order_id INT PRIMARY KEY ,
     order_detail VARCHAR(225),
     CUSTOMER_ID VARCHAR(225),
     PRODUCT_ID VARCHAR(225),
     STORE_ID VARCHAR(225),
     Order_Date date,
     SALES FLOAT,
     QUANTITY INT,
     Discount FLOAT,
     PROFIT FLOAT,
     SHIP_COST FLOAT

)
"""

drop_CUSTOMER_TABLE_SQL = """
       DROP TABLE IF EXISTS DIM_CUSTOMERS;
"""
drop_PRODUCT_TABLE_SQL = """
       DROP TABLE IF EXISTS DIM_PRODUCT;
"""
drop_STORE_TABLE_SQL ="""
     DROP TABLE IF EXISTS DIM_STORE;
"""
drop_FACTSALES_TABLE_SQL = """
      DROP TABLE IF EXISTS FACT_SALES;
"""