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

df_sql_a = pd.read_sql_table('product_a', sqlengine)	# relatively fast than `con= DATABASE_URL`
print("A read SQL table successfully!")
df_sql_b = pd.read_sql_table('product_b', sqlengine)	# relatively fast than `con= DATABASE_URL`
print("B read SQL table successfully!")
df_sql_c = pd.read_sql_table('product_c', sqlengine)	# relatively fast than `con= DATABASE_URL`
print("C read SQL table successfully!")
df_sql_d = pd.read_sql_table('product_d', sqlengine)	# relatively fast than `con= DATABASE_URL`
print("D read SQL table successfully!")
df_sql_e = pd.read_sql_table('product_e', sqlengine)	# relatively fast than `con= DATABASE_URL`
print("E read SQL table successfully!")

print("\n--------------------------------------------")

# ===============================Write dataframe to CSV==============================
# Write to CSVs
df_sql_a.to_csv('../keys/A.csv', index= False)
print("A downloaded to CSV successfully!")
df_sql_b.to_csv('../keys/B.csv', index= False)
print("B downloaded to CSV successfully!")
df_sql_c.to_csv('../keys/C.csv', index= False)
print("C downloaded to CSV successfully!")
df_sql_d.to_csv('../keys/D.csv', index= False)
print("D downloaded to CSV successfully!")
df_sql_e.to_csv('../keys/E.csv', index= False)
print("E downloaded to CSV successfully!")
