# keyhubbot
A key provider to End users based on their data

## Modules
### Phase-1
* #### Commands:
	- `/start`: shows the basic commands
	- `/help`: shows about the bot, description about each commands incorporated
	- `/requestkey`: requesting key --> then select product type - A or B
	- `/keystatus`: view key usage stats for each product
		+ `datetime` - at last access
		+ `location` - accessed from which location (i.e. country) during last time
		+ `keycount` - no. of times keys accessed till date
	- `/sharephone` - share user's phone no. via keyboard 
* #### Location:
* #### Database:
	- __Redis (NoSQL)__:
		+ This database is for viewing the info.s corresponding to a user (with phone no.)
		+ store latest used product keys, key_count_total, key_count_today,
	- __Excel (SQL)__:
		+ This database is for viewing the info.s corresponding to a product key.
		+ This is also for ease of use by the end product manager. They can view the product keys with user details filled correspondingly.

### Phase-2
* <u>__user's daily usage limit:__</u> Here, user's daily usage will be monitored and if exceeds the limit i.e. 2 keys/day, then wait for the next day or subscribe for premium membership.
* <u>__sequential product key dispersal:__</u> A user can avail the product key only if the info. shared in this sequence - `[username --> location]`
* segregate b/w key_count_total, key_count_today

