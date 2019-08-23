"""
    This file - `db.py` is to check the database data.
"""

import redis
from input import REDIS_URL


# ---------------------------------------------------------------
# define Redis database
r = redis.from_url(REDIS_URL)

# ----------------------------------------------------------------
# Access the database values as per the key provided
print(r.hgetall("abhi3700"))    # returns '{}'

print(r.hget("abhi3700", "username").decode('utf-8'))
