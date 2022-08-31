import astral, astral.sun, astral.moon
from datetime import datetime
import pytz
from . import ipinfo

def get_sun_moon():
        
    loc = ipinfo.get_lat_lon()
    latitude = loc["lat"]
    longitude = loc["long"] 
    tz =pytz.timezone(loc["timezone"])
    altitude = 0
    local = datetime.now()
    l = astral.LocationInfo('Custom Name', 'My Region', tz, latitude, longitude)
    s = astral.sun.sun(l.observer, date=local)
    sun_moon ={
        "sunrise" : s['sunrise'].astimezone(tz),
        "sunset" : s['sunset'].astimezone(tz),
        "dawn" :   s['dawn'].astimezone(tz),
        "dusk" : s['dusk'].astimezone(tz),
        "moon" : astral.moon.phase(local)
    }
    return sun_moon
