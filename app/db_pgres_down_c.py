"""
Download the SQL table as dataframe
write the dataframe to CSV
"""
import pandas as pd
import sqlalchemy
from input import cfg_uri_psql

print("===================Status===================")

# ==============================Download dataframe from PostgreSQL table=============
sqlengine = sqlalchemy.create_engine(cfg_uri_psql)

df_sql_c = pd.read_sql_table('product_c', sqlengine)    # relatively fast than `con= DATABASE_URL`
print("C read SQL table successfully!")

print("\n--------------------------------------------")

# ===============================Write dataframe to CSV==============================
# Write to CSVs
df_sql_c.to_csv('../keys/C.csv', index= False)
print("C downloaded to CSV successfully!")