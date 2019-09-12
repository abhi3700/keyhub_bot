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

df_sql_d = pd.read_sql_table('product_d', sqlengine)    # relatively fast than `con= DATABASE_URL`
print("D read SQL table successfully!")

print("\n--------------------------------------------")

# ===============================Write dataframe to CSV==============================
# Write to CSVs
df_sql_d.to_csv('../keys/D.csv', index= False)
print("D downloaded to CSV successfully!")