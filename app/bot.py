import botogram
import redis
# import os
import requests
from input import *


bot = botogram.create(API_key)
bot.about = "This is a Key Provider Bot. \nThis provides keys (max. 2 per day) to a user based on information - username, location"
bot.owner = "@abhi3700"
# ----------------------------------------------------------------------------------------------------------------------------------------
# define Redis database
r = redis.from_url(REDIS_URL)

# =========================================================================================================================================
@bot.command("requestkey")
def requestkey_command(chat, message, args):
    """
    TODO: Check if the user is/not in a channel
    If(message.sender.group != group_name):
        chat.send("You need to be in the group,\n" + group_link + " in order to get key")
    else:
        chat.send("Okay! But I need some of your information. \nUse /sendinfo command.")
    """
    """Provides key based on user information"""
    """User has to click a button for giving information - Username, Location"""
    btns = botogram.Buttons()
    
    btns[0].callback("Product A", "producta")     # button - Product A
    btns[1].callback("Product B", "productb")     # button - Product B

    chat.send("Okay! Select one of the products below -", attach= btns)

# =======================================================Products===========================================================================
@bot.callback("producta")
def producta_callback(query, chat, message):
    chat.send("Okay! But I need some of your information. \nUse /sendinfo command.")

@bot.callback("productb")
def productb_callback(query, chat, message):
    chat.send("Okay! But I need some of your information. \nUse /sendinfo command.")

# ========================================================User Information==================================================================
"""
TODO: Button popping from below
    - Username: when clicked, `username` saved in the database & show msg: "Username noted."
    - Location: When clicked, `location` saved in the database & show msg: "Location noted."
"""
@bot.command("sendinfo")
def sendinfo_command(chat, message, args):
    """User has to click a button for giving information - Username, Location"""
    btns = botogram.Buttons()
    
    btns[0].callback("Username", "username")     # button - Username
    btns[1].callback("Location", "location")     # button - Location
    
    chat.send("Please, click on the buttons in this sequence: \n1. Username \n2. Location", attach= btns)

# define empty dictionary for JSON object in Redis db
# d_username = {}
# =========================================================Parameters==============================================================
@bot.callback("username")
def username_callback(query, chat, message):
    user = query.sender
    username = user.username
    phoneno = username.contact.phone_no

    # r.hmset(username, dict(username= username))
    msg_username = ""   # initialize
    # msg_username = r.hget(username, "username").decode('utf-8')
    msg_username = username 

    query.notify("username: {username} saved.".format(username=msg_username))
    chat.send("Phone no.: {phone} saved.".format(phone= phoneno))
    # chat.send("{username} saved.".format(username=msg_username))
    # chat.send("Now, please share your location by clicking the BUTTON above")

@bot.callback("location")
def location_callback(query, chat, message):
    response = requests.get(geo_URL, verify= False)
    response_json = response.json()     # type - 'dict'
    msg_loc = ""       # initialize
    if response.status_code == 200:
        msg_loc = "Country: {country} saved.".format(country= response_json.get("country_name"))
        # chat.send(msg_loc)
        query.notify(msg_loc)

        # Fetch 'product_key' from DB (in excel) with username & country & phone as empty.
        chat.send("your key is <product_key>")
    else:
        chat.send("Connection ERROR! Please try again later. \nAlso, you can raise query at @abhi3700")
    
# ======================================================Key Usage Stats==========================================================
@bot.command("keystatus")
def keystatus_command(chat, message, args):
    # phone_no = message.contact.phone_no

    """
    TODO:
        Fetch the stats from Redis database 
    """
    chat.send("The key usage stats for product A is <product_a>")
    chat.send("The key usage stats for product B is <product_b>")


    
# ================================================MAIN===========================================================================
if __name__ == "__main__":
    bot.run()