"""
Upload the CSV file to Postgres DB.
each `.csv` file to each `table` 
"""
import pandas as pd
import d6tstack.utils as du
from input import cfg_uri_psql

print("===================Status===================")

# ==============================Read CSV into dataframe=============
df_b = pd.read_csv('../keys/B.csv')
print("B read CSV successfully!")

print("\n--------------------------------------------")

# ==============================Upload dataframe to PostgreSQL database=============
du.pd_to_psql(df_b, cfg_uri_psql, 'product_b', if_exists='replace')
print("B uploaded to SQL successfully!")