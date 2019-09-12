"""
Upload the CSV file to Postgres DB.
each `.csv` file to each `table` 
"""
import pandas as pd
import d6tstack.utils as du
from input import cfg_uri_psql

print("===================Status===================")

# ==============================Read CSV into dataframe=============
df_a = pd.read_csv('../keys/A.csv')
print("A read CSV successfully!")

print("\n--------------------------------------------")

# ==============================Upload dataframe to PostgreSQL database=============
du.pd_to_psql(df_a, cfg_uri_psql, 'product_a', if_exists='replace')
print("A uploaded to SQL successfully!")

