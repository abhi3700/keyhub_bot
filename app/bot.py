import botogram
from input import *

bot = botogram.create(API_key)
bot.about = "This is a Key Provider Bot. \nThis provides keys (max. 6 per day) to a user based on information - date, time, user, country"
bot.owner = "@abhi3700"

# =========================================================================================================================================
@bot.command("requestkey")
def requestkey_command(chat, message, args):
    """
    TODO: Check if the group is/not in a group
    If(message.sender.group != group_name):
        chat.send("You need to be in the group,\n" + group_link + " in order to get key")
    else:
        chat.send("Okay! But I need some of your information. \nUse /sendinfo command.")
    """
    """Provides key based on user information"""
    chat.send("Okay! But I need some of your information. \nUse /sendinfo command.")

"""
parse the function o/p as argument into `btns.callback` line
"data":  string
"return": string
"""
def save_username(data):
    db_status = ""
    return db_status

"""
TODO: Button popping from below
    - Username: when clicked, `username` saved in the database & show msg: "Username noted."
    - Datetime: when clicked, `Datetime` saved in the database & show msg: "Datetime noted."
    - Location: When clicked, `location` saved in the database & show msg: "Location noted."
"""
@bot.command("sendinfo")
def sendinfo_command(chat, message):
    """User has to click a button for giving information - Username, Datetime, Location"""
    btns = botogram.Buttons()
    # TODO: replace `message.sender.username` with `save_username(message.sender.username)`
    btns[0].callback("Username", "username", message.sender.username)     # button - Username
    btns[1].callback("Location", "location", message.sender.location.longitude + message.sender.location.longitude)     # button - Location
    chat.send("Please, select one of the buttons popping below.", attach= btns)

@bot.callback("username")
def username_callback(query, data):
    # query.notify("<username> saved.")
    query.notify("<username>: " + data + " saved." + type(data))
    # query.notify("<username>: " + type(data) + " saved.")

@bot.callback("location")
def location_callback(query, data):
    query.notify("<location>: " + data + " saved." + type(data))
    # query.notify("<location> saved.")

# ================================================MAIN===========================================================================
if __name__ == "__main__":
    bot.run()