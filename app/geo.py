"""
    M-1: Here, `ipdata` has been used.
    M-2: Take the (lat, lon) using Telegram service and then convert into address using Geocoding/Reverse Geocoding via Geocoding API of Google.
        - Refer: https://developers.google.com/maps/documentation/geocoding/start#get-a-key 
"""
# M-1: This takes the location of a server (like Heroku), as it is deployed there.
# import requests

# geo_URL = 'https://api.ipdata.co/?api-key=858097a26b070972fd6ecabb3f36421ff55eaf8337143a4b15ecaf39'

# response = requests.get(geo_URL, verify= False)
# response_json = response.json()     # type - 'dict'

# if response.status_code == 200:
#     print(response_json.get("country_name"))
# else:
#     print("Connection ERROR!")

# ====================================================================================================
# M-2
import requests
from input import google_str_geo

lat = 30.704026
lon = 76.681145

geo_URL = google_str_geo.format(lat= lat, lon= lon)

response = requests.get(geo_URL, verify= False)

response_json = response.json()

# print(response.status_code)
print(response_json["status"])
print(response_json["results"][0]["address_components"][6]["long_name"])

# if response_json["status"] == "OK":
#     print("connection established")

if lat != "":
    print("empty lat")