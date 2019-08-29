"""
TODO:
Test the followings:
- [ ] fetch the product key where all 'country', 'username', 'phoneno' are NaN
- [ ] write the 'country', 'username', 'phoneno' values to CSV file
- [ ] fetch the product keys where df["username"] == 'abhi3700'
"""
import pandas as pd
import numpy as np

df_a = pd.read_csv("../keys/A.csv")
print(df_a.head())
# print(df_a['country'].tolist())
# print(df_a['username'].tolist())
# print(df_a['phoneno'].tolist())

df_b = pd.read_csv("../keys/B.csv")
print(df_b.head())

print(df_a.loc[~(df_a['country'] == 'india')]['phoneno'])

# print(np.nan)

# print(df_a[~(df_a['country'] is np.nan) & ~(df_a['username'] is np.nan) & ~(df_a['phoneno'] is np.nan)])
print(df_a.loc[(df_a['country'] == np.nan)]['phoneno'])

# print(df_a_new.head())

