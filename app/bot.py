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

# -------------------------------------------------------'phone' global var------------------------------------------------------------------------
phone_global = ""      # replace with "" string in production release

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
    """Share your phone no. via clicking the available below."""
    bot.api.call('sendMessage', {
        'chat_id': chat.id,
        'text': 'Please click on keyboard below to share your phone no.',
        'reply_markup': json.dumps({
            'keyboard': [
                [
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

# @bot.message_matches('Phone')
# def action_a_clicked(chat):
#     chat.send('Processing Action A... This won\'t trigger @bot.process_message')


@bot.process_message
def button_messages_are_like_normal_messages(chat, message):
    # if message.text:
    #     chat.send('You choose %s' % message.text)
    # elif message.location:
    #     chat.send('You choose to send your location: %s %s' % (message.location.latitude, message.location.longitude))
    if message.contact:
        # TODO: store/update `phone` in Redis database
        phone_global = message.contact.phone_number
        chat.send('You choose to send your contact: %s' % phone_global)
        chat.send("Okay! But I need some of your information. \nUse /requestkey command.")

    chat.send('Press /removekeyboard to remove the annoying keyboard')

@bot.command("removekeyboard")
def removekeyboard_command(chat, message):
    """removes the keyboard appearing below"""
    bot.api.call('sendMessage', {
        'chat_id': chat.id,
        'reply_to_message': message.id,
        'text': 'keyboard removed.',
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
    # TODO: call `phone` from Redis database
    if phone_global != "":
        """
        TODO: Check if the user is/not in a channel
        If(message.sender.group != group_name):
            chat.send("You need to be in the group,\n" + group_link + " in order to get key")
        else:
            chat.send("Okay! But I need some of your information. \nUse /sendinfo command.")
        """
        btns = botogram.Buttons()
        
        btns[0].callback("Product A", "producta")     # button - Product A
        btns[1].callback("Product B", "productb")     # button - Product B
        btns[2].callback("Product C", "productc")     # button - Product C
        btns[3].callback("Product D", "productd")     # button - Product D
        btns[4].callback("Product E", "producte")     # button - Product E

        chat.send("Okay! Select one of the products below -", attach= btns)
    else:
        chat.send("Please, share the phone no. first via /sharephone")
        chat.send("phone no. is: {phone}".format(phone= phone_global))  # for DEBUG

# # ----------------------------------------------------------------Products------------------------------------------------------------------
@bot.callback("producta")
def producta_callback(query, chat, message):
    chat.send("Now, please share your details --> [username, location] via /sendinfoa command.")

@bot.callback("productb")
def productb_callback(query, chat, message):
    chat.send("Now, please share your details --> [username, location] via /sendinfob command.")

@bot.callback("productc")
def productc_callback(query, chat, message):
    chat.send("Now, please share your details --> [username, location] via /sendinfoc command.")

@bot.callback("productd")
def productd_callback(query, chat, message):
    chat.send("Now, please share your details --> [username, location] via /sendinfod command.")

@bot.callback("producte")
def producte_callback(query, chat, message):
    chat.send("Now, please share your details --> [username, location] via /sendinfoe command.")

# ========================================================User Information for Product A==================================================================
@bot.command("sendinfoa")
def sendinfoa_command(chat, message, args):
    """User has to click a 'Info.' button for giving information"""
    btns = botogram.Buttons()
    
    btns[0].callback("Info.", "shareinfoa")     # button - Username
    # btns[1].callback("Location", "locationa")     # button - Location
    
    chat.send("Please, click on the button below", attach= btns)


# ========================================================User Information for Product B==================================================================
@bot.command("sendinfob")
def sendinfob_command(chat, message, args):
    """User has to click a 'Info.' button for giving information"""
    btns = botogram.Buttons()
    
    btns[0].callback("Info.", "shareinfob")     # button - Username
    # btns[1].callback("Location", "locationa")     # button - Location
    
    chat.send("Please, click on the button below", attach= btns)

# ========================================================User Information for Product C==================================================================
@bot.command("sendinfoc")
def sendinfoc_command(chat, message, args):
    """User has to click a 'Info.' button for giving information"""
    btns = botogram.Buttons()
    
    btns[0].callback("Info.", "shareinfoc")     # button - Username
    # btns[1].callback("Location", "locationa")     # button - Location
    
    chat.send("Please, click on the button below", attach= btns)

# ========================================================User Information for Product D==================================================================
@bot.command("sendinfod")
def sendinfod_command(chat, message, args):
    """User has to click a 'Info.' button for giving information"""
    btns = botogram.Buttons()
    
    btns[0].callback("Info.", "shareinfod")     # button - Username
    # btns[1].callback("Location", "locationa")     # button - Location
    
    chat.send("Please, click on the button below", attach= btns)

# ========================================================User Information for Product E==================================================================
@bot.command("sendinfoe")
def sendinfoe_command(chat, message, args):
    """User has to click a 'Info.' button for giving information"""
    btns = botogram.Buttons()
    
    btns[0].callback("Info.", "shareinfoe")     # button - Username
    # btns[1].callback("Location", "locationa")     # button - Location
    
    chat.send("Please, click on the button below", attach= btns)

# =========================================================User Infos==============================================================
@bot.callback("shareinfoa")
def shareinfoa_callback(query, chat, message):
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

            # Read the SQL table
            df_sql_a = pd.read_sql_table('product_a', sqlengine)

            # Fetch 'product_key' from DB (in excel) with username & country & phone as empty.
            df_nan = df_sql_a[(df_sql_a['country'].isnull()) & (df_sql_a['username'].isnull()) & (df_sql_a['phone'].isnull())]
            ind = df_nan.index.tolist()[0]
            key = df_nan.loc[ind, 'keys']
            chat.send("your key is \n{productkey}".format(productkey= key))

            # Now, note the key, datetime in Redis DB
            r.hset(phone_global, "ProductA", json.dumps(dict(key= key)))
            r.hset(phone_global, "ProductA", json.dumps(dict(datetime= datetime.date.today())))

            # After this, corresponding to this product_key save infos. - username, location, phone is filled in Excel DB.
            df_nan.at[ind, 'country'] = country_name
            df_nan.at[ind, 'username'] = json.loads(r.hget(phone_global, "ProductA").decode('utf-8')).get("username")
            df_nan.at[ind, 'phone'] = phone_global

            # replace the ith row (as per index) of df_sql_a (for e.g.) with df_nan
            df_sql_a.loc[ind] = df_nan.loc[ind]

            # write the modified dataframe to PostgreSQL table
            du.pd_to_psql(df_sql_a, cfg_uri_psql, 'product_a', if_exists='replace')
            chat.send("user details saved in PostgreSQL")   # for DEBUG

        else:
            chat.send("Connection ERROR! Please try again later.\nAlso, you can raise query at @abhi3700")
    else:
        chat.send("Please, share the phone no. first\n")

@bot.callback("shareinfob")
def shareinfob_callback(query, chat, message):
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

            # Read the SQL table
            df_sql_b = pd.read_sql_table('product_b', sqlengine)

            # Fetch 'product_key' from DB (in excel) with username & country & phone as empty.
            df_nan = df_sql_b[(df_sql_b['country'].isnull()) & (df_sql_b['username'].isnull()) & (df_sql_b['phone'].isnull())]
            ind = df_nan.index.tolist()[0]
            key = df_nan.loc[ind, 'keys']
            chat.send("your key is \n{productkey}".format(productkey= key))

            # Now, note the key, datetime in Redis DB
            r.hset(phone_global, "ProductB", json.dumps(dict(key= key)))
            r.hset(phone_global, "ProductB", json.dumps(dict(datetime= datetime.date.today())))
            
            # After this, corresponding to this product_key save infos. - username, location, phone is filled in Excel DB.
            df_nan.at[ind, 'country'] = country_name
            df_nan.at[ind, 'username'] = json.loads(r.hget(phone_global, "ProductB").decode('utf-8')).get("username")
            df_nan.at[ind, 'phone'] = phone_global

            # replace the ith row (as per index) of df_sql_a (for e.g.) with df_nan
            df_sql_b.loc[ind] = df_nan.loc[ind]

            # write the modified dataframe to PostgreSQL table
            du.pd_to_psql(df_sql_b, cfg_uri_psql, 'product_b', if_exists='replace')

        else:
            chat.send("Connection ERROR! Please try again later.\nAlso, you can raise query at @abhi3700")
    else:
        chat.send("Please, share the phone no. first via /sharephone")

@bot.callback("shareinfoc")
def shareinfoc_callback(query, chat, message):
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

            # Read the SQL table
            df_sql_c = pd.read_sql_table('product_c', sqlengine)

            # Fetch 'product_key' from DB (in excel) with username & country & phone as empty.
            df_nan = df_sql_c[(df_sql_c['country'].isnull()) & (df_sql_c['username'].isnull()) & (df_sql_c['phone'].isnull())]
            ind = df_nan.index.tolist()[0]
            key = df_nan.loc[ind, 'keys']
            chat.send("your key is \n{productkey}".format(productkey= key))

            # Now, note the key, datetime in Redis DB
            r.hset(phone_global, "ProductC", json.dumps(dict(key= key)))
            r.hset(phone_global, "ProductC", json.dumps(dict(datetime= datetime.date.today())))
            
            # After this, corresponding to this product_key save infos. - username, location, phone is filled in Excel DB.
            df_nan.at[ind, 'country'] = country_name
            df_nan.at[ind, 'username'] = json.loads(r.hget(phone_global, "ProductC").decode('utf-8')).get("username")
            df_nan.at[ind, 'phone'] = phone_global

            # replace the ith row (as per index) of df_sql_a (for e.g.) with df_nan
            df_sql_c.loc[ind] = df_nan.loc[ind]

            # write the modified dataframe to PostgreSQL table
            du.pd_to_psql(df_sql_c, cfg_uri_psql, 'product_c', if_exists='replace')

        else:
            chat.send("Connection ERROR! Please try again later.\nAlso, you can raise query at @abhi3700")
    else:
        chat.send("Please, share the phone no. first via /sharephone")

@bot.callback("shareinfod")
def shareinfod_callback(query, chat, message):
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

            # Read the SQL table
            df_sql_d = pd.read_sql_table('product_d', sqlengine)

            # Fetch 'product_key' from DB (in excel) with username & country & phone as empty.
            df_nan = df_d[(df_d['country'].isnull()) & (df_d['username'].isnull()) & (df_d['phone'].isnull())]
            ind = df_nan.index.tolist()[0]
            key = df_nan.loc[ind, 'keys']
            chat.send("your key is \n{productkey}".format(productkey= key))

            # Now, note the key, datetime in Redis DB
            r.hset(phone_global, "ProductD", json.dumps(dict(key= key)))
            r.hset(phone_global, "ProductD", json.dumps(dict(datetime= datetime.date.today())))
            
            # After this, corresponding to this product_key save infos. - username, location, phone is filled in Excel DB.
            df_nan.at[ind, 'country'] = country_name
            df_nan.at[ind, 'username'] = json.loads(r.hget(phone_global, "ProductD").decode('utf-8')).get("username")
            df_nan.at[ind, 'phone'] = phone_global

            # replace the ith row (as per index) of df_sql_a (for e.g.) with df_nan
            df_d.loc[ind] = df_nan.loc[ind]

            # write the modified dataframe to PostgreSQL table
            du.pd_to_psql(df_sql_d, cfg_uri_psql, 'product_d', if_exists='replace')

        else:
            chat.send("Connection ERROR! Please try again later.\nAlso, you can raise query at @abhi3700")
    else:
        chat.send("Please, share the phone no. first via /sharephone")

@bot.callback("shareinfoe")
def shareinfoe_callback(query, chat, message):
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

            # Read the SQL table
            df_sql_e = pd.read_sql_table('product_e', sqlengine)

            # Fetch 'product_key' from DB (in excel) with username & country & phone as empty.
            df_nan = df_sql_e[(df_sql_e['country'].isnull()) & (df_sql_e['username'].isnull()) & (df_sql_e['phone'].isnull())]
            ind = df_nan.index.tolist()[0]
            key = df_nan.loc[ind, 'keys']
            chat.send("your key is \n{productkey}".format(productkey= key))

            # Now, note the key, datetime in Redis DB
            r.hset(phone_global, "ProductE", json.dumps(dict(key= key)))
            r.hset(phone_global, "ProductE", json.dumps(dict(datetime= datetime.date.today())))
            
            # After this, corresponding to this product_key save infos. - username, location, phone is filled in Excel DB.
            df_nan.at[ind, 'country'] = country_name
            df_nan.at[ind, 'username'] = json.loads(r.hget(phone_global, "ProductE").decode('utf-8')).get("username")
            df_nan.at[ind, 'phone'] = phone_global

            # replace the ith row (as per index) of df_sql_a (for e.g.) with df_nan
            df_sql_e.loc[ind] = df_nan.loc[ind]

            # write the modified dataframe to PostgreSQL table
            du.pd_to_psql(df_sql_e, cfg_uri_psql, 'product_', if_exists='replace')

        else:
            chat.send("Connection ERROR! Please try again later.\nAlso, you can raise query at @abhi3700")
    else:
        chat.send("Please, share the phone no. first via /sharephone")
# ======================================================Key Usage Stats==========================================================
@bot.command("keystatsa")
def keystatsa_command(chat, message, args):
    """shows the key stats of 'Product A'"""
    """
    TODO:
        Fetch the stats from Excel database 
    """
    uname = message.sender.username

    df_search = df_sql_a.loc[df_sql_a['username'].isin([uname])]

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

    df_search = df_sql_b.loc[df_sql_b['username'].isin([uname])]

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

    df_search = df_sql_c.loc[df_sql_c['username'].isin([uname])]

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

    df_search = df_sql_e.loc[df_sql_e['username'].isin([uname])]

    if len(df_search) != 0:
        chat.send("The keys accessed so far:")
        for k in range(len(df_search)):
            chat.send("{key}\n".format(key= df_search['keys'].tolist()[k]))
    else:
        chat.send("No product keys accessed.")
    
# ================================================MAIN===========================================================================
if __name__ == "__main__":
    bot.run()