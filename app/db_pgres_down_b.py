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

df_sql_b = pd.read_sql_table('product_b', sqlengine)    # relatively fast than `con= DATABASE_URL`
print("B read SQL table successfully!")

print("\n--------------------------------------------")

# ===============================Write dataframe to CSV==============================
# Write to CSVs
df_sql_b.to_csv('../keys/B.csv', index= False)
print("B downloaded to CSV successfully!")
