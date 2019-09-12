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
df_b = pd.read_csv('../keys/B.csv')
print("B read CSV successfully!")
df_c = pd.read_csv('../keys/C.csv')
print("C read CSV successfully!")
df_d = pd.read_csv('../keys/D.csv')
print("D read CSV successfully!")
df_e = pd.read_csv('../keys/E.csv')
print("E read CSV successfully!")

print("\n--------------------------------------------")

# ==============================Upload dataframe to PostgreSQL database=============
du.pd_to_psql(df_a, cfg_uri_psql, 'product_a', if_exists='replace')
print("A uploaded to SQL successfully!")
du.pd_to_psql(df_b, cfg_uri_psql, 'product_b', if_exists='replace')
print("B uploaded to SQL successfully!")
du.pd_to_psql(df_c, cfg_uri_psql, 'product_c', if_exists='replace')
print("C uploaded to SQL successfully!")
du.pd_to_psql(df_d, cfg_uri_psql, 'product_d', if_exists='replace')
print("D uploaded to SQL successfully!")
du.pd_to_psql(df_e, cfg_uri_psql, 'product_e', if_exists='replace')
print("E uploaded to SQL successfully!")