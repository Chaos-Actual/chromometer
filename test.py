import requests as req
from dotenv import load_dotenv
import os

#enviroment variables
load_dotenv()
IPINFO_TOKEN =os.getenv('IPINFO_TOKEN')

url = f'http://ipinfo.io/json?token={IPINFO_TOKEN}'

x = {'ip': '98.30.188.15', 'hostname': 'cpe-98-30-188-15.cinci.res.rr.com', 
'city': 'Georgetown', 'region': 'Indiana', 'country': 'US', 'loc': '38.2945,-85.9755',
 'org': 'AS10796 Charter Communications Inc', 'postal': '47122', 
 'timezone': 
 'America/Kentucky/Louisville'}

resp = req.get(url)
if(resp.status_code != 200):
    print('ERROR! Response Code'+resp)
else:
    j_resp = resp.json()
    print(j_resp)
    loc = j_resp["loc"].split(",")
lat= loc[0]
long = loc[1]
print(lat)
print(long)


