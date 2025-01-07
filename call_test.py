import openmeteo_requests
import requests_cache
import pandas as pd
import dates_to_call, gps_coords_to_call
from pandas.core.interchange import dataframe
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
open_meteo = openmeteo_requests.Client(session = retry_session)

latitude = 43.04
longitude = -87.91
start_date = "2025-01-04"
end_date = "2025-01-05"
timezone = "CST"

url = "https://archive-api.open-meteo.com/v1/archive"
params = {
		"latitude": latitude,
		"longitude": longitude,
		"start_date": start_date,
		"end_date": end_date,
		"hourly": ["temperature_2m", "precipitation", "cloud_cover", "wind_speed_100m"],
		"timezone": timezone,
        "temperature_unit": "fahrenheit"
	}
responses = open_meteo.weather_api(url, params=params)

print(responses[0])