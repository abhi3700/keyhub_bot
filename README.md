# keyhubbot
A key provider to End users based on their data

## Python Packages
* `botogram2`
* `redis`
* `requests`
* `pandas`
* `numpy`
* `sqlalchemy`
* `d6tstack`
* `psycopg2`

> NOTE: for uploading a package u need an additional pkg: `d6tstack` 


## Modules
### Phase-1
* #### Commands:
	- `/start`: shows the basic commands
	- `/help`: shows about the bot, description about each commands incorporated
	- `/requestkey`: requesting key --> then select product type - A or B
	- `/shareinfoa`: User has to share info for product-A key access
	- `/keystatus`: view key usage stats for each product
		+ `datetime` - at last access
		+ `location` - accessed from which location (i.e. country) during last time
		+ `keycount` - no. of times keys accessed till date
	- `/sharephone` - share user's phone no. via keyboard
	- `/shareloc` - share user's location via keyboard
* #### Location:
	- The location coordinates is accessed via Telegram service and the same is reverse geocoded using Google Geocoding API service.
	- refer: `geo.py` file for testing.
	- Currently (with botogram v0.6), it was not possible to access the location inside `shareinfoa` command. And that's why a `datetoday` param has been stored in `"info"` dict_key.
* #### Database:
	- __Redis (NoSQL)__:
		+ This database is for viewing the info.s corresponding to a user (with phone no.)
		+ store latest used product keys, key_count_total, key_count_today,
	- __PostgreSQL (SQL)__:
		+ This database is for viewing the info.s (username, phone, country) corresponding to a product key.
		+ This is also for ease of use by the product manager. They can view the product keys with user details filled correspondingly.

### Phase-2
* <u>__user's daily usage limit:__</u> Here, user's daily usage will be monitored and if exceeds the limit i.e. 2 keys/day, then wait for the next day or subscribe for premium membership.
	- Here, store the params `keycount_today`, `keycount_total` in `"product_a"` root for product-A.
* <u>__sequential product key dispersal:__</u> A user can avail the product key only if the info. shared in this sequence - `[username --> location]`
* segregate b/w key_count_total, key_count_today

## Troubleshooting
* PostgreSQL Database ERROR
	- Just keep your default browser logged in with Heroku account, as created service from here.
