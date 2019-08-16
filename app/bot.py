import botogram
from input import *

bot = botogram.create(API_key)
bot.about = "This is a Key Provider Bot. \nThis provides keys (max. 6 per day) to a user based on information - date, time, user, country"
bot.owner = "@abhi3700"

@bot.command("requestkey")
def requestkey_command(chat, message, args):
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
    btns[0].callback("Username", "username")
    chat.send("Please, select one of the buttons popping below.", attach= btns)

@bot.callback("username")
def username_callback(query, chat, message):
    # chat.send("<username> Noted.")
    query.notify("<username> Noted.")

if __name__ == "__main__":
    bot.run()