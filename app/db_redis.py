"""
    This file - `db.py` is to check the database data.
"""

import redis
import datetime
import json
from input import REDIS_URL


# ---------------------------------------------------------------
# define Redis database
r = redis.from_url(REDIS_URL)

# ----------------------------------------------------------------
phoneno = "8143243443"
username = "abhi3700"
country = "India"

product_a = dict(username= username, country= country, key_count= 3, datetime= str(datetime.date.today()))
r.hset(phoneno, "ProductA", json.dumps(product_a))

product_b = dict(username= username, country= country, key_count= 5, datetime= str(datetime.date.today()))
r.hset(phoneno, "ProductB", json.dumps(product_b))

print(r.hget(phoneno, "ProductA").decode('utf-8'))
print(r.hget(phoneno, "ProductB").decode('utf-8'))


# count the key
newkey = json.loads(r.hget(phoneno, "ProductA").decode('utf-8')).get("key_count") + 1
print(newkey)

# json.loads() converts from string to dictionary. This is to access the get() function
print(json.loads(r.hget(phoneno, "ProductA").decode('utf-8')).get("username"))
# print(json.dumps(r.get(phoneno), indent= 2))
for key in r.keys():
    # print(key.decode('utf-8'))
    print(json.loads(r.hget(key.decode('utf-8'), "ProductA").decode('utf-8')).get('username'))
