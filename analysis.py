from geopy import Nominatim

from call_for_data import make_master_dataframe
from gps_coords_to_call import convert_location_to_gps
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def localize_dataframe(dataframe):
    """
    Takes a dataframe, converts times to local, then groups by hour for analysis
    :param dataframe:
    :return:
    """
    dataframe['local'] = dataframe['date'].dt.tz_localize('utc').dt.tz_convert('America/Chicago')
    dataframe = dataframe.drop('date', axis=1)
    dataframe['Dates'] = pd.to_datetime(dataframe['local']).dt.date
    dataframe['Time'] = pd.to_datetime(dataframe['local']).dt.time
    dataframe = dataframe.drop('local', axis=1)
    return dataframe


if __name__ == "__main__":
    location = "baltimore"
    month = 3
    day = 7
    gps = convert_location_to_gps(location)
    df1 = make_master_dataframe(gps, month, day)
    workable_data = localize_dataframe(df1)
    print(workable_data)