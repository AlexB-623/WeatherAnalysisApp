# importing geopy library and Nominatim class
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
import datetime

# calling the Nominatim tool and create Nominatim class
loc = Nominatim(user_agent="Geopy Library")

def convert_location_to_gps(location):
    """
    takes a string and tries to determine if it is a known city.
    if it is, it will return GPS coordinates for that city as a Tuple, otherwise, returns a string with an error message.
    :param location: string
    :return: tuple: (lat, long, timezone) OR string with an error message.
    """
    getloc = loc.geocode(location)
    try:
        lat = round(float(getloc.latitude), 3)
        long = round(float(getloc.longitude), 3)
    except AttributeError:
        return "Could not convert the entered location name to GPS\n" \
                "Please check the spelling and try again"
    return lat, long

def get_timezone(latitude, longitude):
    obj = TimezoneFinder()
    # returns 'Europe/Berlin'
    result = obj.timezone_at(lat=latitude, lng=longitude)
    return result



if __name__ == "__main__":
    test_mke = convert_location_to_gps("milwaukee")
    print(f'Milwaukee GPS coords are {test_mke}')

if __name__ == "__main__":
    lat = 43.04
    long = -87.91
    tz = get_timezone(lat, long)
    print(f'the timezone for lat {lat} and long {long} is {tz}')

if __name__ == "__main__":
    tz = "America/Chicago"

if __name__ == '__main__':
    broken = "laksjdf;ja;sldiem"
    test_broken = convert_location_to_gps(broken)
    print(f'the gps coords for {broken} are: {test_broken}')

if __name__ == '__main__':
    baltimore = "baltimore"
    baltimore_md = "baltimore, md"
    baltimore_oh = "baltimore, oh"
    print(f'Baltimore = { convert_location_to_gps(baltimore) }')
    print(f'Baltimore MD = {convert_location_to_gps(baltimore_md)}')
    print(f'Baltimore OH = {convert_location_to_gps(baltimore_oh)}')