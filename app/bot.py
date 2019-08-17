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
TODO: Button popping from below
    - Username: when clicked, `username` saved in the database & show msg: "Username noted."
    - Datetime: when clicked, `Datetime` saved in the database & show msg: "Datetime noted."
    - Location: When clicked, `location` saved in the database & show msg: "Location noted."
"""
@bot.command("sendinfo")
def sendinfo_command(chat, message, args):
    """User has to click a button for giving information - Username, Datetime, Location"""
    btns = botogram.Buttons()
    
    btns[0].callback("Username", "username")     # button - Username
    btns[1].callback("Location", "location")     # button - Location
    
    chat.send("Please, select one of the buttons popping below.", attach= btns)

@bot.callback("username")
def username_callback(query, chat, message):
    user = query.sender
    chat.send(user.username)    # test 
    query.notify("{username} saved.".format(username=user.username))

@bot.callback("location")
def location_callback(query, chat, message, location):
    loc = location
    lat = loc.latitude
    lng = loc.longitude
    chat.send(str(lat) + " & " + str(lng))      # test
    query.notify("{latitude} & {longitude} saved.".format(latitude=str(lat), longitude=str(lng)))

# ================================================MAIN===========================================================================
if __name__ == "__main__":
    bot.run()