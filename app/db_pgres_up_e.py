"""
Upload the CSV file to Postgres DB.
each `.csv` file to each `table` 
"""
import pandas as pd
import d6tstack.utils as du
from input import cfg_uri_psql

print("===================Status===================")

# ==============================Read CSV into dataframe=============
df_e = pd.read_csv('../keys/E.csv')
print("E read CSV successfully!")

print("\n--------------------------------------------")

# ==============================Upload dataframe to PostgreSQL database=============
du.pd_to_psql(df_e, cfg_uri_psql, 'product_e', if_exists='replace')
print("E uploaded to SQL successfully!")