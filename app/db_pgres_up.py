"""
Upload the CSV file to Postgres DB.
each `.csv` file to each `table` 
"""
import pandas as pd
import d6tstack.utils as du
from input import *


df_a = pd.read_csv('../keys/A.csv')
df_b = pd.read_csv('../keys/B.csv')
df_c = pd.read_csv('../keys/C.csv')
df_d = pd.read_csv('../keys/D.csv')
df_e = pd.read_csv('../keys/E.csv')


du.pd_to_psql(df_a, cfg_uri_psql, 'product_a', if_exists='replace')
du.pd_to_psql(df_b, cfg_uri_psql, 'product_b', if_exists='replace')
du.pd_to_psql(df_c, cfg_uri_psql, 'product_c', if_exists='replace')
du.pd_to_psql(df_d, cfg_uri_psql, 'product_d', if_exists='replace')
du.pd_to_psql(df_e, cfg_uri_psql, 'product_e', if_exists='replace')