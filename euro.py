import requests
import json

resp = requests.get('https://restcountries.eu/rest/v2/region/europe')
for t in resp.json():
    r = t['regionalBlocs']
    for a in r:
     print(a['name'])