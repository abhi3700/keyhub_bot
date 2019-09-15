import botogram
import redis
import requests
import json
import pandas as pd
import numpy as np
import datetime
import sqlalchemy
import d6tstack.utils as du
from input import *


# -------------------------------------------------------About Bot--------------------------------------------------------------------
bot = botogram.create(API_key)
bot.about = "This is a Key Provider Bot. \nThis provides keys (max. 2 per day) to a user based on information - username, location"
bot.owner = "@abhi3700"
# -------------------------------------------------------Redis DB------------------------------------------------------------------------
# define Redis database
r = redis.from_url(REDIS_URL)


# -------------------------------------------------------initialize SQL engine for PostgreSQL------------------------------------------------------------------------
sqlengine = sqlalchemy.create_engine(cfg_uri_psql)

# =======================================================Share phone via keyboard===========================================================================
@bot.command("sharephone")
def sharephone_command(chat, message, args):
    """Share your phone no. via clicking the keyboard below."""
    bot.api.call('sendMessage', {
        'chat_id': chat.id,
        'text': 'Please click on keyboard below to share your phone no.',
        'reply_markup': json.dumps({
            'keyboard': [
                [
                    # {
                    #     'text': 'location',
                    #     'request_location': True,
                    # },
                    {
                        'text': 'Phone no.',
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

@bot.command("shareloc")
def shareloc_command(chat, message, args):
    """Share your location via clicking the keyboard below."""
    bot.api.call('sendMessage', {
        'chat_id': chat.id,
        'text': 'Please click on keyboard below to share your location',
        'reply_markup': json.dumps({
            'keyboard': [
                [
                    {
                        'text': 'location',
                        'request_location': True,
                    },
                    # {
                    #     'text': 'Phone no.',
                    #     'request_contact': True,
                    # },
                ],
            ],
            # These 3 parameters below are optional
            # See https://core.telegram.org/bots/api#replykeyboardmarkup
            'resize_keyboard': True,
            'one_time_keyboard': True,
            'selective': True,
        }),
    })

# @bot.message_matches('Phone')
# def action_a_clicked(chat):
#     chat.send('Processing Action A... This won\'t trigger @bot.process_message')


@bot.process_message
def button_messages_are_like_normal_messages(chat, message):
    # if message.text:
    #     chat.send('You choose %s' % message.text)
    if message.contact:
        phoneno = message.contact.phone_number
        phoneno = phoneno.replace("+", "")      # '+91343242343' --> '91343242343'Unlike phone app, in Telegram desktop app, it's '+' sign in phone no.

        # Create a node - `phone` and store `username` in REDIS DB. This is bcoz in botogram, can't set global_variable.
        r.hset(phoneno, "info", json.dumps(dict(username= message.sender.username)))

        # find the root phoneno. if username is available in REDIS DB
        key_phone = ""
        for k in r.keys():
            # print(k.decode('utf-8'))
            dict_nested2_val2 = json.loads(r.hget(k.decode('utf-8'), "info"))
            if dict_nested2_val2['username'] == message.sender.username:
                key_phone = k.decode('utf-8')

        chat.send('You choose to send your contact no.: {phone}'.format(phone= key_phone))
        chat.send("Now, please share your location via /shareloc")
        # chat.send("Okay! But I need some of your information. \nUse /requestkey command.")

    elif message.location:
        # find the root phoneno. if username is available in REDIS DB
        key_phone = ""
        for k in r.keys():
            # print(k.decode('utf-8'))
            dict_nested2_val2 = json.loads(r.hget(k.decode('utf-8'), "info"))
            if dict_nested2_val2['username'] == message.sender.username:
                key_phone = k.decode('utf-8')

        if key_phone != "":
            # Create a node - `phone` and store `username`, `latitude`, `longitude` in REDIS DB. This is bcoz in botogram, can't set global_variable.
            r.hset(key_phone, "info", json.dumps(dict(username= message.sender.username,
                                                     lat= message.location.latitude,
                                                     lon= message.location.longitude,
                                                     datetoday= str(datetime.date.today()))))

            # chat.send('You choose to send your location: %s %s' % (message.location.latitude, message.location.longitude))
            chat.send("Okay! But I need some of your information. \nUse /requestkey command.")
        else:
            chat.send("Please, share the phone no. first via /sharephone")

    chat.send('Press /removekeyboard to remove the annoying keyboard')

@bot.command("removekeyboard")
def removekeyboard_command(chat, message):
    """removes the keyboard appearing below"""
    bot.api.call('sendMessage', {
        'chat_id': chat.id,
        'reply_to_message': message.id,
        'text': 'keyboards removed.',
        'reply_markup': json.dumps({
            'remove_keyboard': True,
            # This 1 parameter below is optional
            # See https://core.telegram.org/bots/api#replykeyboardremove
            'selective': True,
        })
    })

# ==============================================================Request key COMMAND=============================================================
@bot.command("requestkey")
def requestkey_command(chat, message, args):
    """request the key for different products"""
    # TODO: call `phone` from Redis database
    key_phone = ""
    for k in r.keys():
        # print(k.decode('utf-8'))
        dict_nested2_val2 = json.loads(r.hget(k.decode('utf-8'), "info"))
        if dict_nested2_val2['username'] == message.sender.username:
            key_phone = k.decode('utf-8')

    if key_phone != "":
        """
        TODO: Check if the user is/not in a channel
        If(message.sender.group != group_name):
            chat.send("You need to be in the group,\n" + group_link + " in order to get key")
        else:
            btns = botogram.Buttons()
            ........
            .......
            ....
        """
        btns = botogram.Buttons()
        
        btns[0].callback("A", "producta")     # button - Product A
        btns[0].callback("B", "productb")     # button - Product B
        # btns[0].callback("C", "productc")     # button - Product C
        # btns[0].callback("D", "productd")     # button - Product D
        # btns[0].callback("E", "producte")     # button - Product E

        chat.send("Okay! Select one of the products below -\nA - Android \nB - Windows", attach= btns)
    else:
        chat.send("Please, share the phone no. first via /sharephone")
        # chat.send("phone no. is: {phone}".format(phone= key_phone))  # for DEBUG

# ----------------------------------------------------------------Product buttons CALLBACK------------------------------------------------------------------
"""
    Here, we could have used `notify_callback` but the data has to be withing 32 characters (ASCII).
    So, used separate callbacks for each product.

@bot.callback("notify")
def notify_callback(query, data, chat, message):
    query.notify(data)
"""
@bot.callback("producta")
def producta_callback(query, chat, message):
    # chat.send("Now, please share your details --> [username, location] via /sendinfoa command.")
    chat.send("Now, please share your details --> [username, location] via /shareinfoa command.")

@bot.callback("productb")
def productb_callback(query, chat, message):
    # chat.send("Now, please share your details --> [username, location] via /sendinfob command.")
    chat.send("Now, please share your details --> [username, location] via /shareinfob command.")

# @bot.callback("productc")
# def productc_callback(query, chat, message):
#     # chat.send("Now, please share your details --> [username, location] via /sendinfoc command.")
#     chat.send("Now, please share your details --> [username, location] via /shareinfoc command.")

# @bot.callback("productd")
# def productd_callback(query, chat, message):
#     # chat.send("Now, please share your details --> [username, location] via /sendinfod command.")
#     chat.send("Now, please share your details --> [username, location] via /shareinfod command.")

# @bot.callback("producte")
# def producte_callback(query, chat, message):
#     # chat.send("Now, please share your details --> [username, location] via /sendinfoe command.")
#     chat.send("Now, please share your details --> [username, location] via /shareinfoe command.")


# =========================================================User Information for Product A==============================================================
@bot.command("shareinfoa")
def shareinfoa_command(chat, message, args):
    """User has to share info for product-A key access"""
    # uname = query.sender.username
    uname = message.sender.username

    # find the root phoneno. if username is available in REDIS DB
    # chat.send('Finding if your username exists with us.....')
    key_phone = ""
    for k in r.keys():
        # print(k.decode('utf-8'))
        dict_nested2_val2 = json.loads(r.hget(k.decode('utf-8'), "info"))
        if dict_nested2_val2['username'] == message.sender.username:
            key_phone = k.decode('utf-8')
    # chat.send("key_phone is: {key_phone}".format(key_phone= key_phone))   # for DEBUG


    if key_phone != "":
        # chat.send("Inside key_phone if-else loop")      # for DEBUG
        # lat = json.loads(r.hget(key_phone, "info").decode('utf-8')).get("lat")
        # lon = json.loads(r.hget(key_phone, "info").decode('utf-8')).get("lon")
        datetoday = json.loads(r.hget(key_phone, "info").decode('utf-8')).get("datetoday")

        """
        Here, to ensure the location is latest (during product key access), datetoday has to be matched with the one stored in "info" dict_key
        """
        if datetoday == str(datetime.date.today()):     # today's date has to be matched with the one stored in "info" dict_key
            # chat.send("Inside location if-else loop")      # for DEBUG

            lat = json.loads(r.hget(key_phone, "info").decode('utf-8')).get("lat")
            lon = json.loads(r.hget(key_phone, "info").decode('utf-8')).get("lon")

            geo_URL = google_str_geo.format(lat= lat, lon= lon)

            response = requests.get(geo_URL, verify= False)
            
            response_json = response.json()     # type - 'dict'
            if response_json["status"] == "OK":
                country_name = response_json["results"][0]["address_components"][-2]["long_name"]
                chat.send('Country: \'{country}\' noted'.format(country= country_name))
                chat.send('Username: \'{username}\' noted'.format(username= uname))

                # Read the SQL table
                chat.send("Please wait...")
                # chat.send("Reading the SQL database. Please wait...")   # for DEBUG
                df_sql = pd.read_sql_table('product_a', sqlengine)

                """ Fetch 'product_key' from DB (in excel) with username & country & phone as empty."""
                df_nan = df_sql[(df_sql['country'].isnull()) & (df_sql['username'].isnull()) & (df_sql['phone'].isnull())]
                
                if len(df_nan) != 0:    # check if `df_nan` is not empty
                    df_nan.fillna('', inplace=True)     # replace 'NaN' with empty/blank string, bcoz when empty `df_nan`, then can't put value due to datatype mismatch (float vs str) 
                    ind = df_nan.index.tolist()[0]
                    key = df_nan.loc[ind, 'keys']
                    chat.send("your key is \n{productkey}".format(productkey= key))

                    """ Now, note the username, country, key, datetime in Redis DB"""
                    r.hset(key_phone, "product_a", 
                        json.dumps(dict(username= uname, 
                                        country= country_name, 
                                        key= key, 
                                        datetime= str(datetime.date.today())
                                        )))

                    """ After this, corresponding to this product_key save infos. - username, location, phone is filled in Excel DB. """
                    # chat.send("replacing [country, username, phone] in the dataframe- `df_nan`. Please wait....")   # for DEBUG
                    df_nan.at[ind, 'country'] = country_name
                    df_nan.at[ind, 'username'] = uname
                    df_nan.at[ind, 'phone'] = key_phone

                    # replace the ith row (as per index) of df_sql (for e.g.) with df_nan
                    df_sql.loc[ind] = df_nan.loc[ind]

                    # write the modified dataframe to PostgreSQL table
                    chat.send("Few more seconds, please.....")
                    # chat.send("Uploading modified dataframe to the SQL database. Please wait....")      # for DEBUG
                    du.pd_to_psql(df_sql, cfg_uri_psql, 'product_a', if_exists='replace')
                    # chat.send("user details saved in PostgreSQL")   # for DEBUG
                    chat.send("DONE! \nFor more, use /help command.")
                else:
                    chat.send("SORRY! \nNo more keys are available. So, please ask @abhi3700 to append more keys.")

            else:
                chat.send("Connection ERROR! Please try again later.\nAlso, you can raise query at @abhi3700")
        else:
            chat.send("Please, share your location via /shareloc")
    else:
        chat.send("Please, share the phone no. first via /sharephone")

# =========================================================User Information for Product A==============================================================
@bot.command("shareinfob")
def shareinfob_command(chat, message, args):
    """User has to share info for product-B key access"""
    # uname = query.sender.username
    uname = message.sender.username

    # find the root phoneno. if username is available in REDIS DB
    # chat.send('Finding if your username exists with us.....')
    key_phone = ""
    for k in r.keys():
        # print(k.decode('utf-8'))
        dict_nested2_val2 = json.loads(r.hget(k.decode('utf-8'), "info"))
        if dict_nested2_val2['username'] == message.sender.username:
            key_phone = k.decode('utf-8')
    # chat.send("key_phone is: {key_phone}".format(key_phone= key_phone))   # for DEBUG


    if key_phone != "":
        # chat.send("Inside key_phone if-else loop")      # for DEBUG
        # lat = json.loads(r.hget(key_phone, "info").decode('utf-8')).get("lat")
        # lon = json.loads(r.hget(key_phone, "info").decode('utf-8')).get("lon")
        datetoday = json.loads(r.hget(key_phone, "info").decode('utf-8')).get("datetoday")

        """
        Here, to ensure the location is latest (during product key access), datetoday has to be matched with the one stored in "info" dict_key
        """
        if datetoday == str(datetime.date.today()):     # today's date has to be matched with the one stored in "info" dict_key
            # chat.send("Inside location if-else loop")      # for DEBUG

            lat = json.loads(r.hget(key_phone, "info").decode('utf-8')).get("lat")
            lon = json.loads(r.hget(key_phone, "info").decode('utf-8')).get("lon")

            geo_URL = google_str_geo.format(lat= lat, lon= lon)

            response = requests.get(geo_URL, verify= False)
            
            response_json = response.json()     # type - 'dict'
            if response_json["status"] == "OK":
                country_name = response_json["results"][0]["address_components"][-2]["long_name"]
                chat.send('Country: \'{country}\' noted'.format(country= country_name))
                chat.send('Username: \'{username}\' noted'.format(username= uname))

                # Read the SQL table
                chat.send("Please wait...")
                # chat.send("Reading the SQL database. Please wait...")   # for DEBUG
                df_sql = pd.read_sql_table('product_b', sqlengine)

                """ Fetch 'product_key' from DB (in excel) with username & country & phone as empty."""
                df_nan = df_sql[(df_sql['country'].isnull()) & (df_sql['username'].isnull()) & (df_sql['phone'].isnull())]
                
                if len(df_nan) != 0:    # check if `df_nan` is not empty
                    df_nan.fillna('', inplace=True)     # replace 'NaN' with empty/blank string, bcoz when empty `df_nan`, then can't put value due to datatype mismatch (float vs str) 
                    ind = df_nan.index.tolist()[0]
                    key = df_nan.loc[ind, 'keys']
                    chat.send("your key is \n{productkey}".format(productkey= key))

                    """ Now, note the username, country, key, datetime in Redis DB"""
                    r.hset(key_phone, "product_b", 
                        json.dumps(dict(username= uname, 
                                        country= country_name, 
                                        key= key, 
                                        datetime= str(datetime.date.today())
                                        )))

                    """ After this, corresponding to this product_key save infos. - username, location, phone is filled in Excel DB. """
                    # chat.send("replacing [country, username, phone] in the dataframe- `df_nan`. Please wait....")   # for DEBUG
                    df_nan.at[ind, 'country'] = country_name
                    df_nan.at[ind, 'username'] = uname
                    df_nan.at[ind, 'phone'] = key_phone

                    # replace the ith row (as per index) of df_sql (for e.g.) with df_nan
                    df_sql.loc[ind] = df_nan.loc[ind]

                    # write the modified dataframe to PostgreSQL table
                    chat.send("Few more seconds, please.....")
                    # chat.send("Uploading modified dataframe to the SQL database. Please wait....")      # for DEBUG
                    du.pd_to_psql(df_sql, cfg_uri_psql, 'product_b', if_exists='replace')
                    # chat.send("user details saved in PostgreSQL")   # for DEBUG
                    chat.send("DONE! \nFor more, use /help command.")
                else:
                    chat.send("SORRY! \nNo more keys are available. So, please ask @abhi3700 to append more keys.")

            else:
                chat.send("Connection ERROR! Please try again later.\nAlso, you can raise query at @abhi3700")
        else:
            chat.send("Please, share your location via /shareloc")
    else:
        chat.send("Please, share the phone no. first via /sharephone")

# ======================================================Key Usage Stats==========================================================
# @bot.command("keystatsa")
# def keystatsa_command(chat, message, args):
#     """shows the key stats of 'Product A'"""
#     """
#     TODO:
#         Fetch the stats from Excel database 
#     """
#     uname = message.sender.username

#     df_search = df_sql.loc[df_sql['username'].isin([uname])]

#     if len(df_search) != 0:
#         chat.send("The keys accessed so far:")
#         for k in range(len(df_search)):
#             chat.send("{key}\n".format(key= df_search['keys'].tolist()[k]))
#     else:
#         chat.send("No product keys accessed.")

# @bot.command("keystatsb")
# def keystatsb_command(chat, message, args):
#     """shows the key stats of 'Product B'"""
#     """
#     TODO:
#         Fetch the stats from Excel database 
#     """
#     uname = message.sender.username

#     df_search = df_sql_b.loc[df_sql_b['username'].isin([uname])]

#     if len(df_search) != 0:
#         chat.send("The keys accessed so far:")
#         for k in range(len(df_search)):
#             chat.send("{key}\n".format(key= df_search['keys'].tolist()[k]))
#     else:
#         chat.send("No product keys accessed.")

# @bot.command("keystatsc")
# def keystatsc_command(chat, message, args):
#     """shows the key stats of 'Product C'"""
#     """
#     TODO:
#         Fetch the stats from Excel database 
#     """
#     uname = message.sender.username

#     df_search = df_sql_c.loc[df_sql_c['username'].isin([uname])]

#     if len(df_search) != 0:
#         chat.send("The keys accessed so far:")
#         for k in range(len(df_search)):
#             chat.send("{key}\n".format(key= df_search['keys'].tolist()[k]))
#     else:
#         chat.send("No product keys accessed.")

# @bot.command("keystatsd")
# def keystatsd_command(chat, message, args):
#     """shows the key stats of 'Product D'"""
#     """
#     TODO:
#         Fetch the stats from Excel database 
#     """
#     uname = message.sender.username

#     df_search = df_d.loc[df_d['username'].isin([uname])]

#     if len(df_search) != 0:
#         chat.send("The keys accessed so far:")
#         for k in range(len(df_search)):
#             chat.send("{key}\n".format(key= df_search['keys'].tolist()[k]))
#     else:
#         chat.send("No product keys accessed.")

# @bot.command("keystatse")
# def keystatse_command(chat, message, args):
#     """shows the key stats of 'Product E'"""
#     """
#     TODO:
#         Fetch the stats from Excel database 
#     """
#     uname = message.sender.username

#     df_search = df_sql_e.loc[df_sql_e['username'].isin([uname])]

#     if len(df_search) != 0:
#         chat.send("The keys accessed so far:")
#         for k in range(len(df_search)):
#             chat.send("{key}\n".format(key= df_search['keys'].tolist()[k]))
#     else:
#         chat.send("No product keys accessed.")

@bot.command("channelstatus")
def channelstatus_command(chat, message, args):
    """shows the channel status of a user - joined or not"""
    status = chat.status_of(int(args[0]))
    chat.send("*%s*" % status)
# ================================================MAIN===========================================================================
if __name__ == "__main__":
    bot.run()