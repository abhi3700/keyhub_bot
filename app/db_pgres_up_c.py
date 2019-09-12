"""
Upload the CSV file to Postgres DB.
each `.csv` file to each `table` 
"""
import pandas as pd
import d6tstack.utils as du
from input import cfg_uri_psql

print("===================Status===================")

# ==============================Read CSV into dataframe=============
df_c = pd.read_csv('../keys/C.csv')
print("C read CSV successfully!")

print("\n--------------------------------------------")

# ==============================Upload dataframe to PostgreSQL database=============
du.pd_to_psql(df_c, cfg_uri_psql, 'product_c', if_exists='replace')
print("C uploaded to SQL successfully!")