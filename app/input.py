# Take it from creating Bot API token in BotFather's chat
API_key = "979871020:AAEDYNWPOm6y3BJaO5u1ojbvtSsYnim2kJM"

# Capture using `$ heroku config | grep REDIS` from the terminal at App's root dir
REDIS_URL = "redis://h:pd4a2fa90f5a63058400930ffd21f5864312b2a174061846e13543a79eb1fdd81@ec2-54-77-8-133.eu-west-1.compute.amazonaws.com:18179"

# Capture using `$ heroku config` from the terminal at App's root dir
DATABASE_URL = "postgres://sncwwevyyzviez:7569a516be40f3f5d62f6d6a8818556771c5f1ade86096b96dabeb01bef14c37@ec2-54-247-96-169.eu-west-1.compute.amazonaws.com:5432/dm8m5ustplad3"
cfg_uri_psql = "postgresql+psycopg2://sncwwevyyzviez:7569a516be40f3f5d62f6d6a8818556771c5f1ade86096b96dabeb01bef14c37@ec2-54-247-96-169.eu-west-1.compute.amazonaws.com:5432/dm8m5ustplad3"

# Accesssing 'country_name' from this reverse geocoding of lat,lon, obtained from Telegram service
google_str_geo = "https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key=AIzaSyDiMMj4cr8_OEREgaTyJjUvAB1Hd38LgLY"
