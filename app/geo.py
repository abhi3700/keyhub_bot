"""
    Here, `ipdata` has been used.
"""
import requests

geo_URL = 'https://api.ipdata.co/?api-key=858097a26b070972fd6ecabb3f36421ff55eaf8337143a4b15ecaf39'

response = requests.get(geo_URL, verify= False)
response_json = response.json()     # type - 'dict'

if response.status_code == 200:
    print(response_json.get("country_name"))
else:
    print("Connection ERROR!")