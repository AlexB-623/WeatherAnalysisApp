import requests, json


def get_year_of_data(start_date, end_date, latitude, longitude, t_unit='fahrenheit'):
    """
    takes the following parameters:
    :param start_date:
    :param end_date:
    :param latitude:
    :param longitude:
    :return: a json object for a "year" of weather data (target day +&- 7 days)
    """
    base_url = f'https://historical-forecast-api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&temperature_unit={t_unit}&hourly=temperature_2m,precipitation,cloud_cover,wind_speed_100m&timezone=auto'
    req = requests.get(base_url)
    json_content = json.loads(req.content)
    return json_content