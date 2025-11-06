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



# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
def call_for_data(latitude, longitude, start_date, end_date):
    """
    calls the openmeteo API for historical weather data
    :param latitude:
    :param longitude:
    :param start_date:
    :param end_date:
    :return:
    """
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
		"latitude": latitude,
		"longitude": longitude,
		"start_date": start_date,
		"end_date": end_date,
		"hourly": ["temperature_2m", "precipitation", "cloud_cover", "wind_speed_100m"],
		"timezone": "auto",
        "temperature_unit": "fahrenheit"
	}
    responses = open_meteo.weather_api(url, params=params)
    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    return response
    #we may want to add some functionality to determine if there was an error with the API response


def make_dataframe(api_response):
    """
    takes the result of call for data and transforms it into a dataframe
    :param api_response:
    :return:
    """
    # we may need to handle NoneType if a given location doesn't have recorded data for a given time
    hourly = api_response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_precipitation = hourly.Variables(1).ValuesAsNumpy()
    hourly_cloud_cover = hourly.Variables(2).ValuesAsNumpy()
    hourly_wind_speed_100m = hourly.Variables(3).ValuesAsNumpy()
    hourly_data = {"date": pd.date_range(
		start = pd.to_datetime(hourly.Time(), unit = "s"),
		end = pd.to_datetime(hourly.TimeEnd(), unit = "s"),
		freq = pd.Timedelta(seconds = hourly.Interval()),
		inclusive = "left"
	)}
    hourly_data["temperature_2m"] = hourly_temperature_2m
    hourly_data["precipitation"] = hourly_precipitation
    hourly_data["cloud_cover"] = hourly_cloud_cover
    hourly_data["wind_speed_100m"] = hourly_wind_speed_100m

    return pd.DataFrame(data = hourly_data)


def make_master_dataframe(input_location, month, day):
    """

    :param input_location: string, city name
    :param month:
    :param day:
    :return: pandas dataframe with weather data for the requested city/date
    """
    is_first_result = True
    location = gps_coords_to_call.convert_location_to_gps(input_location)
    if type(location) == str:
        return location
    years_to_call = dates_to_call.generate_master_date_list(month, day)
    for year in years_to_call:
        year_data = call_for_data(latitude=location[0], longitude=location[1], start_date=year[-1], end_date=year[0])
        if is_first_result:
            master_dataframe = make_dataframe(year_data)
            is_first_result = False
        else:
            year_dataframe = make_dataframe(year_data)
            master_dataframe = pd.concat([master_dataframe, year_dataframe])
            year_dataframe = None
    return master_dataframe

if __name__ == "__main__":
    milwaukee = make_master_dataframe("milwaukee", 6, 23)
    print(f'Working test: The results for milwaukee are: \n {milwaukee}')

if __name__ == "__main__":
    milwaukee = make_master_dataframe("auekxkne", 6, 23)
    print(f'Broken test: The results for milwaukee are: \n {milwaukee}')