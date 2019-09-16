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

lat = 5.360361
lon = 76.453654

geo_URL = google_str_geo.format(lat= lat, lon= lon)

response = requests.get(geo_URL, verify= False)

response_json = response.json()

# print(response.status_code)
print(response_json["status"])
# print(response_json["results"][0]["address_components"][-2]["long_name"])   # accessing from last
print(response_json["results"][0]["formatted_address"])
print(response_json["results"][0]["formatted_address"].split(',')[-1].strip())

# if response_json["status"] == "OK":
#     print("connection established")

# if lat != "":
#     print("empty lat")

# ====================================================================================================
# M-3
# import requests
# from input import nominatim_str_geo

# lat = 30.704026
# lon = 76.681145

# geo_URL = nominatim_str_geo.format(lat= lat, lon= lon)

# response = requests.get(geo_URL, verify= False)

# response_json = response.json()
# print(response_json)

# print(response_json["address"]["country"])

# JSON output
"""
{
    "place_id":142501739,
    "licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
    "osm_type":"way",
    "osm_id":279767995,
    "lat":"40.7141281",
    "lon":"-73.9613111",
    "place_rank":30,
    "category":"building",
    "type":"yes",
    "importance":0,
    "addresstype":"building",
    "name":null,
    "display_name":"281, Bedford Avenue, Williamsburg, Brooklyn, Kings County, New York, 11211, USA",
    "address":{
        "house_number":"281",
        "road":"Bedford Avenue",
        "neighbourhood":"Williamsburg",
        "suburb":"Brooklyn",
        "county":"Kings County",
        "city":"New York",
        "state":"New York",
        "postcode":"11211",
        "country":"USA",
        "country_code":"us"
    },
    "boundingbox":["40.714064","40.7141922","-73.9614164","-73.9612058"]
}
"""