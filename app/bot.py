import botogram
import redis
import requests
import json
import pandas as pd
import numpy as np
import datetime
from input import *

# -------------------------------------------------------About Bot--------------------------------------------------------------------
bot = botogram.create(API_key)
bot.about = "This is a Key Provider Bot. \nThis provides keys (max. 2 per day) to a user based on information - username, location"
bot.owner = "@abhi3700"
# -------------------------------------------------------Redis DB------------------------------------------------------------------------
# define Redis database
r = redis.from_url(REDIS_URL)

# -------------------------------------------------------'phone' global var------------------------------------------------------------------------
phone_global = "DUMMY"      # replace with "" string in production release

# -------------------------------------------------------Excel CSV dataframes------------------------------------------------------------------------
df_a = pd.read_csv('../keys/A.csv')
df_b = pd.read_csv('../keys/B.csv')
df_c = pd.read_csv('../keys/C.csv')
df_d = pd.read_csv('../keys/D.csv')
df_e = pd.read_csv('../keys/E.csv')

# =======================================================Share phone via keyboard===========================================================================
@bot.command("sharephone")
def sharephone_command(chat, message, args):
    """Share your phone no. via clicking the available below."""
    bot.api.call('sendMessage', {
        'chat_id': chat.id,
        'text': 'Please click on keyboard below to share your phone no.',
        'reply_markup': json.dumps({
            'keyboard': [
                [
                    {'text': 'Phone'},
                ],
                [
                    {
                        'text': 'Share your phone number',
                        'request_contact': True,
                    },
                ],
            ],
            # These 3 parameters below are optional
            # See https://core.telegram.org/bots/api#replykeyboardmarkup
            'resize_keyboard': True,
            'one_time_keyboard': True,
            'selective': True,
        }),
    })

@bot.message_matches('Phone')
def action_a_clicked(chat):
    chat.send('Processing Action A... This won\'t trigger @bot.process_message')


@bot.process_message
def button_messages_are_like_normal_messages(chat, message):
    # if message.text:
    #     chat.send('You choose %s' % message.text)
    # elif message.location:
    #     chat.send('You choose to send your location: %s %s' % (message.location.latitude, message.location.longitude))
    if message.contact:
        phone_global = message.contact.phone_number
        chat.send('You choose to send your contact: %s' % message.contact.phone_number)
        chat.send("Okay! But I need some of your information. \nUse /requestkey command.")

    chat.send('Press /removekeyboard to remove the annoying keyboard')

@bot.command("removekeyboard")
def removekeyboard_command(chat, message):
    """removes the keyboard appearing below"""
    bot.api.call('sendMessage', {
        'chat_id': chat.id,
        'reply_to_message': message.id,
        'text': 'This message removes the keyboard',
        'reply_markup': json.dumps({
            'remove_keyboard': True,
            # This 1 parameter below is optional
            # See https://core.telegram.org/bots/api#replykeyboardremove
            'selective': True,
        })
    })

# ==============================================================Request key=============================================================
@bot.command("requestkey")
def requestkey_command(chat, message, args):
    """request the key for different products"""
    if phone_global != "":
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
        btns[2].callback("Product C", "productc")     # button - Product C
        btns[3].callback("Product D", "productd")     # button - Product D
        btns[4].callback("Product E", "producte")     # button - Product E

        chat.send("Okay! Select one of the products below -", attach= btns)
    else:
        chat.send("Please, share the phone no. first\n")

# ----------------------------------------------------------------Products------------------------------------------------------------------
@bot.callback("producta")
def producta_callback(query, chat, message):
    chat.send("First of all, please share your phone no. via /sendinfoa command.")

@bot.callback("productb")
def productb_callback(query, chat, message):
    chat.send("First of all, please share your phone no. via /sendinfob command.")

@bot.callback("productc")
def producta_callback(query, chat, message):
    chat.send("First of all, please share your phone no. via /sendinfoc command.")

@bot.callback("productd")
def producta_callback(query, chat, message):
    chat.send("First of all, please share your phone no. via /sendinfod command.")

@bot.callback("producte")
def producta_callback(query, chat, message):
    chat.send("First of all, please share your phone no. via /sendinfoe command.")

# ========================================================User Information for Product A==================================================================
"""
TODO: Button popping from below
    - Username: when clicked, `username` saved in the database & show msg: "Username noted."
    - Location: When clicked, `location` saved in the database & show msg: "Location noted."
"""
@bot.command("sendinfoa")
def sendinfo_command(chat, message, args):
    """User has to click a button for giving information - Username, Location"""
    btns = botogram.Buttons()
    
    btns[0].callback("Info.", "shareinfoa")     # button - Username
    # btns[1].callback("Location", "locationa")     # button - Location
    
    chat.send("Please, click on the buttons popping below", attach= btns)


# ========================================================User Information for Product B==================================================================
"""
TODO: Button popping from below
    - Username: when clicked, `username` saved in the database & show msg: "Username noted."
    - Location: When clicked, `location` saved in the database & show msg: "Location noted."
"""
@bot.command("sendinfob")
def sendinfo_command(chat, message, args):
    """User has to click a button for giving information - Username, Location"""
    btns = botogram.Buttons()
    
    btns[0].callback("Info.", "shareinfob")     # button - Username
    # btns[1].callback("Location", "locationa")     # button - Location
    
    chat.send("Please, click on the buttons popping below", attach= btns)

# ========================================================User Information for Product C==================================================================
"""
TODO: Button popping from below
    - Username: when clicked, `username` saved in the database & show msg: "Username noted."
    - Location: When clicked, `location` saved in the database & show msg: "Location noted."
"""
@bot.command("sendinfoc")
def sendinfo_command(chat, message, args):
    """User has to click a button for giving information - Username, Location"""
    btns = botogram.Buttons()
    
    btns[0].callback("Info.", "shareinfoc")     # button - Username
    # btns[1].callback("Location", "locationa")     # button - Location
    
    chat.send("Please, click on the buttons popping below", attach= btns)

# ========================================================User Information for Product D==================================================================
"""
TODO: Button popping from below
    - Username: when clicked, `username` saved in the database & show msg: "Username noted."
    - Location: When clicked, `location` saved in the database & show msg: "Location noted."
"""
@bot.command("sendinfod")
def sendinfo_command(chat, message, args):
    """User has to click a button for giving information - Username, Location"""
    btns = botogram.Buttons()
    
    btns[0].callback("Info.", "shareinfod")     # button - Username
    # btns[1].callback("Location", "locationa")     # button - Location
    
    chat.send("Please, click on the buttons popping below", attach= btns)

# ========================================================User Information for Product E==================================================================
"""
TODO: Button popping from below
    - Username: when clicked, `username` saved in the database & show msg: "Username noted."
    - Location: When clicked, `location` saved in the database & show msg: "Location noted."
"""
@bot.command("sendinfoe")
def sendinfo_command(chat, message, args):
    """User has to click a button for giving information - Username, Location"""
    btns = botogram.Buttons()
    
    btns[0].callback("Info.", "shareinfoe")     # button - Username
    # btns[1].callback("Location", "locationa")     # button - Location
    
    chat.send("Please, click on the buttons popping below", attach= btns)

# =========================================================User Infos==============================================================
@bot.callback("shareinfoa")
def location_callback(query, chat, message):
    user = query.sender
    uname = user.username

    response = requests.get(geo_URL, verify= False)
    response_json = response.json()     # type - 'dict'

    if phone_global != "":
        if response.status_code == 200:
            country_name = response_json.get("country_name")

            r.hset(phone_global, "ProductA", json.dumps(dict(username= uname)))
            r.hset(phone_global, "ProductA", json.dumps(dict(country= country_name)))

            query.notify("country: {country} saved.".format(country= json.loads(r.hget(phone_global, "ProductA").decode('utf-8')).get("country")))

            # Fetch 'product_key' from DB (in excel) with username & country & phone as empty.
            df_nan = df_a[(df_a['country'].isnull()) & (df_a['username'].isnull()) & (df_a['phoneno'].isnull())]
            ind = df_nan.index.tolist()[0]
            key = df_nan.loc[ind, 'keys']
            chat.send("your key is \n{productkey}".format(productkey= key))

            # Now, note the key, datetime in Redis DB
            r.hset(phone_global, "ProductA", json.dumps(dict(key= key)))
            r.hset(phone_global, "ProductA", json.dumps(dict(datetime= datetime.date.today())))

            # After this, corresponding to this product_key save infos. - username, location, phoneno is filled in Excel DB.
            df_nan.at[ind, 'country'] = country_name
            df_nan.at[ind, 'username'] = json.loads(r.hget(phone_global, "ProductA").decode('utf-8')).get("username")
            df_nan.at[ind, 'phoneno'] = phone_global

            # replace the ith row (as per index) of df_a (for e.g.) with df_nan
            df_a.loc[ind] = df_nan.loc[ind]

            # write the details to product CSV file
            df_a.to_csv('keys/A.csv', index= False)

        else:
            chat.send("Connection ERROR! Please try again later.\nAlso, you can raise query at @abhi3700")
    else:
        chat.send("Please, share the phone no. first\n")

@bot.callback("shareinfob")
def location_callback(query, chat, message):
    user = query.sender
    uname = user.username

    response = requests.get(geo_URL, verify= False)
    response_json = response.json()     # type - 'dict'

    if phone_global != "":
        if response.status_code == 200:
            country_name = response_json.get("country_name")

            r.hset(phone_global, "ProductB", json.dumps(dict(username= uname)))
            r.hset(phone_global, "ProductB", json.dumps(dict(country= country_name)))

            query.notify("country: {country} saved.".format(country= json.loads(r.hget(phone_global, "ProductB").decode('utf-8')).get("country")))

            # Fetch 'product_key' from DB (in excel) with username & country & phone as empty.
            df_nan = df_b[(df_b['country'].isnull()) & (df_b['username'].isnull()) & (df_b['phoneno'].isnull())]
            ind = df_nan.index.tolist()[0]
            key = df_nan.loc[ind, 'keys']
            chat.send("your key is \n{productkey}".format(productkey= key))

            # Now, note the key, datetime in Redis DB
            r.hset(phone_global, "ProductB", json.dumps(dict(key= key)))
            r.hset(phone_global, "ProductB", json.dumps(dict(datetime= datetime.date.today())))
            
            # After this, corresponding to this product_key save infos. - username, location, phoneno is filled in Excel DB.
            df_nan.at[ind, 'country'] = country_name
            df_nan.at[ind, 'username'] = json.loads(r.hget(phone_global, "ProductB").decode('utf-8')).get("username")
            df_nan.at[ind, 'phoneno'] = phone_global

            # replace the ith row (as per index) of df_a (for e.g.) with df_nan
            df_b.loc[ind] = df_nan.loc[ind]

            # write the details to product CSV file
            df_b.to_csv('keys/B.csv', index= False)

        else:
            chat.send("Connection ERROR! Please try again later.\nAlso, you can raise query at @abhi3700")
    else:
        chat.send("Please, share the phone no. first\n")

@bot.callback("shareinfoc")
def location_callback(query, chat, message):
    user = query.sender
    uname = user.username

    response = requests.get(geo_URL, verify= False)
    response_json = response.json()     # type - 'dict'

    if phone_global != "":
        if response.status_code == 200:
            country_name = response_json.get("country_name")

            r.hset(phone_global, "ProductC", json.dumps(dict(username= uname)))
            r.hset(phone_global, "ProductC", json.dumps(dict(country= country_name)))

            query.notify("country: {country} saved.".format(country= json.loads(r.hget(phone_global, "ProductC").decode('utf-8')).get("country")))

            # Fetch 'product_key' from DB (in excel) with username & country & phone as empty.
            df_nan = df_c[(df_c['country'].isnull()) & (df_c['username'].isnull()) & (df_c['phoneno'].isnull())]
            ind = df_nan.index.tolist()[0]
            key = df_nan.loc[ind, 'keys']
            chat.send("your key is \n{productkey}".format(productkey= key))

            # Now, note the key, datetime in Redis DB
            r.hset(phone_global, "ProductC", json.dumps(dict(key= key)))
            r.hset(phone_global, "ProductC", json.dumps(dict(datetime= datetime.date.today())))
            
            # After this, corresponding to this product_key save infos. - username, location, phoneno is filled in Excel DB.
            df_nan.at[ind, 'country'] = country_name
            df_nan.at[ind, 'username'] = json.loads(r.hget(phone_global, "ProductC").decode('utf-8')).get("username")
            df_nan.at[ind, 'phoneno'] = phone_global

            # replace the ith row (as per index) of df_a (for e.g.) with df_nan
            df_c.loc[ind] = df_nan.loc[ind]

            # write the details to product CSV file
            df_c.to_csv('keys/C.csv', index= False)

        else:
            chat.send("Connection ERROR! Please try again later.\nAlso, you can raise query at @abhi3700")
    else:
        chat.send("Please, share the phone no. first\n")

@bot.callback("shareinfod")
def location_callback(query, chat, message):
    user = query.sender
    uname = user.username

    response = requests.get(geo_URL, verify= False)
    response_json = response.json()     # type - 'dict'

    if phone_global != "":
        if response.status_code == 200:
            country_name = response_json.get("country_name")

            r.hset(phone_global, "ProductD", json.dumps(dict(username= uname)))
            r.hset(phone_global, "ProductD", json.dumps(dict(country= country_name)))

            query.notify("country: {country} saved.".format(country= json.loads(r.hget(phone_global, "ProductD").decode('utf-8')).get("country")))

            # Fetch 'product_key' from DB (in excel) with username & country & phone as empty.
            df_nan = df_d[(df_d['country'].isnull()) & (df_d['username'].isnull()) & (df_d['phoneno'].isnull())]
            ind = df_nan.index.tolist()[0]
            key = df_nan.loc[ind, 'keys']
            chat.send("your key is \n{productkey}".format(productkey= key))

            # Now, note the key, datetime in Redis DB
            r.hset(phone_global, "ProductD", json.dumps(dict(key= key)))
            r.hset(phone_global, "ProductD", json.dumps(dict(datetime= datetime.date.today())))
            
            # After this, corresponding to this product_key save infos. - username, location, phoneno is filled in Excel DB.
            df_nan.at[ind, 'country'] = country_name
            df_nan.at[ind, 'username'] = json.loads(r.hget(phone_global, "ProductD").decode('utf-8')).get("username")
            df_nan.at[ind, 'phoneno'] = phone_global

            # replace the ith row (as per index) of df_a (for e.g.) with df_nan
            df_d.loc[ind] = df_nan.loc[ind]

            # write the details to product CSV file
            df_d.to_csv('keys/D.csv', index= False)

        else:
            chat.send("Connection ERROR! Please try again later.\nAlso, you can raise query at @abhi3700")
    else:
        chat.send("Please, share the phone no. first\n")

@bot.callback("shareinfoe")
def location_callback(query, chat, message):
    user = query.sender
    uname = user.username

    response = requests.get(geo_URL, verify= False)
    response_json = response.json()     # type - 'dict'

    if phone_global != "":
        if response.status_code == 200:
            country_name = response_json.get("country_name")

            r.hset(phone_global, "ProductE", json.dumps(dict(username= uname)))
            r.hset(phone_global, "ProductE", json.dumps(dict(country= country_name)))

            query.notify("country: {country} saved.".format(country= json.loads(r.hget(phone_global, "ProductE").decode('utf-8')).get("country")))

            # Fetch 'product_key' from DB (in excel) with username & country & phone as empty.
            df_nan = df_e[(df_e['country'].isnull()) & (df_e['username'].isnull()) & (df_e['phoneno'].isnull())]
            ind = df_nan.index.tolist()[0]
            key = df_nan.loc[ind, 'keys']
            chat.send("your key is \n{productkey}".format(productkey= key))

            # Now, note the key, datetime in Redis DB
            r.hset(phone_global, "ProductE", json.dumps(dict(key= key)))
            r.hset(phone_global, "ProductE", json.dumps(dict(datetime= datetime.date.today())))
            
            # After this, corresponding to this product_key save infos. - username, location, phoneno is filled in Excel DB.
            df_nan.at[ind, 'country'] = country_name
            df_nan.at[ind, 'username'] = json.loads(r.hget(phone_global, "ProductE").decode('utf-8')).get("username")
            df_nan.at[ind, 'phoneno'] = phone_global

            # replace the ith row (as per index) of df_a (for e.g.) with df_nan
            df_e.loc[ind] = df_nan.loc[ind]

            # write the details to product CSV file
            df_e.to_csv('keys/E.csv', index= False)

        else:
            chat.send("Connection ERROR! Please try again later.\nAlso, you can raise query at @abhi3700")
    else:
        chat.send("Please, share the phone no. first\n")

# ======================================================Key Usage Stats==========================================================
@bot.command("keystatsa")
def keystatsa_command(chat, message, args):
    """shows the key stats of 'Product A'"""
    """
    TODO:
        Fetch the stats from Excel database 
    """
    uname = message.sender.username

    df_search = df_a.loc[df_a['username'].isin([uname])]

    if len(df_search) != 0:
        chat.send("The keys accessed so far:")
        for k in range(len(df_search)):
            chat.send("{key}\n".format(key= df_search['keys'].tolist()[k]))
    else:
        chat.send("No product keys accessed.")

@bot.command("keystatsb")
def keystatsb_command(chat, message, args):
    """shows the key stats of 'Product B'"""
    """
    TODO:
        Fetch the stats from Excel database 
    """
    uname = message.sender.username

    df_search = df_b.loc[df_b['username'].isin([uname])]

    if len(df_search) != 0:
        chat.send("The keys accessed so far:")
        for k in range(len(df_search)):
            chat.send("{key}\n".format(key= df_search['keys'].tolist()[k]))
    else:
        chat.send("No product keys accessed.")

@bot.command("keystatsc")
def keystatsc_command(chat, message, args):
    """shows the key stats of 'Product C'"""
    """
    TODO:
        Fetch the stats from Excel database 
    """
    uname = message.sender.username

    df_search = df_c.loc[df_c['username'].isin([uname])]

    if len(df_search) != 0:
        chat.send("The keys accessed so far:")
        for k in range(len(df_search)):
            chat.send("{key}\n".format(key= df_search['keys'].tolist()[k]))
    else:
        chat.send("No product keys accessed.")

@bot.command("keystatsd")
def keystatsd_command(chat, message, args):
    """shows the key stats of 'Product D'"""
    """
    TODO:
        Fetch the stats from Excel database 
    """
    uname = message.sender.username

    df_search = df_d.loc[df_d['username'].isin([uname])]

    if len(df_search) != 0:
        chat.send("The keys accessed so far:")
        for k in range(len(df_search)):
            chat.send("{key}\n".format(key= df_search['keys'].tolist()[k]))
    else:
        chat.send("No product keys accessed.")

@bot.command("keystatse")
def keystatse_command(chat, message, args):
    """shows the key stats of 'Product E'"""
    """
    TODO:
        Fetch the stats from Excel database 
    """
    uname = message.sender.username

    df_search = df_e.loc[df_e['username'].isin([uname])]

    if len(df_search) != 0:
        chat.send("The keys accessed so far:")
        for k in range(len(df_search)):
            chat.send("{key}\n".format(key= df_search['keys'].tolist()[k]))
    else:
        chat.send("No product keys accessed.")
    
# ================================================MAIN===========================================================================
if __name__ == "__main__":
    bot.run()