import requests as req
from dotenv import load_dotenv
import os

#enviroment variables
load_dotenv()
IPINFO_TOKEN =os.getenv('IPINFO_TOKEN')

url = f'http://ipinfo.io/json?token={IPINFO_TOKEN}'

def get_lat_lon():
    resp = req.get(url)
    if(resp.status_code != 200):
        print('ERROR! Response Code'+resp)
    else:
        j_resp = resp.json()
        ll = j_resp["loc"].split(",")
        loc = { 
            "lat" : ll[0],
            "long": ll[1],
            "timezone" : j_resp["timezone"]
        }
    return loc
