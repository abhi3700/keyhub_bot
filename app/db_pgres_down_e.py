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

df_sql_e = pd.read_sql_table('product_e', sqlengine)    # relatively fast than `con= DATABASE_URL`
print("E read SQL table successfully!")

print("\n--------------------------------------------")

# ===============================Write dataframe to CSV==============================
# Write to CSVs
df_sql_e.to_csv('../keys/E.csv', index= False)
print("E downloaded to CSV successfully!")
