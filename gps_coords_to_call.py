# importing geopy library and Nominatim class
from geopy.geocoders import Nominatim

# calling the Nominatim tool and create Nominatim class
loc = Nominatim(user_agent="Geopy Library")

def convert_location_to_gps(location):
    """
    takes a string and tries to determine if it is a known city.
    if it is, it will return GPS coordinates for that city
    :param location:
    :return: tuple: (lat, long)
    """
    getloc = loc.geocode(location)
    try:
        lat = round(float(getloc.latitude), 2)
        long = round(float(getloc.longitude), 2)
    except AttributeError:
        return "Could not convert the entered location name to GPS\n" \
                "Please check the spelling and try again"
    return lat, long