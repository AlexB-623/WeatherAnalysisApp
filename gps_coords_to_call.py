# importing geopy library and Nominatim class
from geopy.geocoders import Nominatim

# calling the Nominatim tool and create Nominatim class
loc = Nominatim(user_agent="Geopy Library")

def convert_location_to_gps(location):
    getloc = loc.geocode(location)
    try:
        lat = round(float(getloc.latitude), 2)
        long = round(float(getloc.longitude), 2)
    except AttributeError:
        return "Could not convert location name to GPS- please check the spelling and try again"
    return lat, long