import time

import pandas as pd
import requests


def add_weather():
    df1 = pd.read_csv('trimmed_merged_file_weather.csv', encoding="ISO-8859-1")
    dest_wcode_array = []
    orig_wcode_array = []
    dest_temperature_2m_max_array = []
    orig_temperature_2m_max_array = []
    dest_temperature_2m_min_array = []
    orig_temperature_2m_min_array = []
    dest_apparent_temperature_max_array = []
    orig_apparent_temperature_max_array = []
    dest_apparent_temperature_min_array = []
    orig_apparent_temperature_min_array = []
    dest_precipitation_hours_array = []
    orig_precipitation_hours_array = []
    dest_sunrise_array = []
    orig_sunrise_array = []
    dest_sunset_array = []
    orig_sunset_array = []
    dest_windspeed_10m_max_array = []
    orig_windspeed_10m_max_array = []
    dest_windgusts_10m_max_array = []
    orig_windgusts_10m_max_array = []
    dest_winddirection_10m_dominant_array = []
    orig_winddirection_10m_dominant_array = []

    for index, row in df1.iterrows():
        if index < 10489:
            continue
        month = row['MONTH']
        if str(month).__len__() == 1:
            month = "0" + str(month)
        else:
            month = str(month)
        day = row['DAY']
        if str(day).__len__() == 1:
            day = "0" + str(day)
        else:
            day = str(day)
        num = 0
        while num == 0:
            try:
                r1 = requests.get("https://archive-api.open-meteo.com/v1/archive?latitude=" + str(row['DESTINATION_LATITUDE']) +
                             "&longitude=" + str(row['DESTINATION_LONGITUDE']) + "&start_date=" +
                             str(row['YEAR']) + "-" + month + "-" + day +
                             "&end_date=" + str(row['YEAR']) + "-" + month + "-" + day + "&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,precipitation_hours,sunrise,sunset,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant&&timezone=America/Anchorage")
                r2 = requests.get("https://archive-api.open-meteo.com/v1/archive?latitude=" + str(row['ORIGIN_LATITUDE']) +
                              "&longitude=" + str(row['ORIGIN_LONGITUDE']) + "&start_date=" +
                              str(row['YEAR']) + "-" + month + "-" + day +
                              "&end_date=" + str(row['YEAR']) + "-" + month + "-" + day + "&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,precipitation_hours,sunrise,sunset,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant&&timezone=America/Anchorage")
                num = 1
            except:
                time.sleep(0.1)

        data1 = r1.json()
        data2 = r2.json()
        print(index)
        try:
            dest_wcode_array.append(data1['daily']['weathercode'][0])
        except:
            dest_wcode_array.append('')
        try:
            orig_wcode_array.append(data2['daily']['weathercode'][0])
        except:
            orig_wcode_array.append('')
        try:
            dest_temperature_2m_max_array.append(data1['daily']['temperature_2m_max'][0])
        except:
            dest_temperature_2m_max_array.append('')
        try:
            orig_temperature_2m_max_array.append(data2['daily']['temperature_2m_max'][0])
        except:
            orig_temperature_2m_max_array.append('')
        try:
            dest_temperature_2m_min_array.append(data1['daily']['temperature_2m_min'][0])
        except:
            dest_temperature_2m_min_array.append('')
        try:
            orig_temperature_2m_min_array.append(data2['daily']['temperature_2m_min'][0])
        except:
            orig_temperature_2m_min_array.append('')
        try:
            dest_apparent_temperature_max_array.append(data1['daily']['apparent_temperature_max'][0])
        except:
            dest_apparent_temperature_max_array.append('')
        try:
            orig_apparent_temperature_max_array.append(data2['daily']['apparent_temperature_max'][0])
        except:
            orig_apparent_temperature_max_array.append('')
        try:
            dest_apparent_temperature_min_array.append(data1['daily']['apparent_temperature_min'][0])
        except:
            dest_apparent_temperature_min_array.append('')
        try:
            orig_apparent_temperature_min_array.append(data2['daily']['apparent_temperature_min'][0])
        except:
            orig_apparent_temperature_min_array.append('')
        try:
            dest_precipitation_hours_array.append(data1['daily']['precipitation_hours'][0])
        except:
            dest_precipitation_hours_array.append('')
        try:
            orig_precipitation_hours_array.append(data2['daily']['precipitation_hours'][0])
        except:
            orig_precipitation_hours_array.append('')
        try:
            dest_sunrise_array.append(data1['daily']['sunrise'][0])
        except:
            dest_sunrise_array.append('')
        try:
            orig_sunrise_array.append(data2['daily']['sunrise'][0])
        except:
            orig_sunrise_array.append('')
        try:
            dest_sunset_array.append(data1['daily']['sunset'][0])
        except:
            dest_sunset_array.append('')
        try:
            orig_sunset_array.append(data2['daily']['sunset'][0])
        except:
            orig_sunset_array.append('')
        try:
            dest_windspeed_10m_max_array.append(data1['daily']['windspeed_10m_max'][0])
        except:
            dest_windspeed_10m_max_array.append('')
        try:
            orig_windspeed_10m_max_array.append(data2['daily']['windspeed_10m_max'][0])
        except:
            orig_windspeed_10m_max_array.append('')
        try:
            dest_windgusts_10m_max_array.append(data1['daily']['windgusts_10m_max'][0])
        except:
            dest_windgusts_10m_max_array.append('')
        try:
            orig_windgusts_10m_max_array.append(data2['daily']['windgusts_10m_max'][0])
        except:
            orig_windgusts_10m_max_array.append('')
        try:
            dest_winddirection_10m_dominant_array.append(data1['daily']['winddirection_10m_dominant'][0])
        except:
            dest_winddirection_10m_dominant_array.append('')
        try:
            orig_winddirection_10m_dominant_array.append(data2['daily']['winddirection_10m_dominant'][0])
        except:
            orig_winddirection_10m_dominant_array.append('')




    # df1['DESTINATION_WCODE'] = dest_wcode_array
    # df1['ORIGIN_WCODE'] = orig_wcode_array
    # df1['DESTINATION_TEMPERATURE_2M_MAX'] = dest_temperature_2m_max_array
    # df1['ORIGIN_TEMPERATURE_2M_MAX'] = orig_temperature_2m_max_array
    # df1['DESTINATION_TEMPERATURE_2M_MIN'] = dest_temperature_2m_min_array
    # df1['ORIGIN_TEMPERATURE_2M_MIN'] = orig_temperature_2m_min_array
    # df1['DESTINATION_APPARENT_TEMPERATURE_MAX'] = dest_apparent_temperature_max_array
    # df1['ORIGIN_APPARENT_TEMPERATURE_MAX'] = orig_apparent_temperature_max_array
    # df1['DESTINATION_APPARENT_TEMPERATURE_MIN'] = dest_apparent_temperature_min_array
    # df1['ORIGIN_APPARENT_TEMPERATURE_MIN'] = orig_apparent_temperature_min_array
    # df1['DESTINATION_PRECIPITATION_HOURS'] = dest_precipitation_hours_array
    # df1['ORIGIN_PRECIPITATION_HOURS'] = orig_precipitation_hours_array
    # df1['DESTINATION_SUNRISE'] = dest_sunrise_array
    # df1['ORIGIN_SUNRISE'] = orig_sunrise_array
    # df1['DESTINATION_SUNSET'] = dest_sunset_array
    # df1['ORIGIN_SUNSET'] = orig_sunset_array
    # df1['DESTINATION_WINDSPEED_10M_MAX'] = dest_windspeed_10m_max_array
    # df1['ORIGIN_WINDSPEED_10M_MAX'] = orig_windspeed_10m_max_array
    # df1['DESTINATION_WINDGUSTS_10M_MAX'] = dest_windgusts_10m_max_array
    # df1['ORIGIN_WINDGUSTS_10M_MAX'] = orig_windgusts_10m_max_array
    # df1['DESTINATION_WINDDIRECTION_10M_DOMINANT_10M_MAX'] = dest_winddirection_10m_dominant_array
    # df1['ORIGIN_WINDDIRECTION_10M_DOMINANT_10M_MAX'] = orig_winddirection_10m_dominant_array


    print('dest_wcode_array')
    print(dest_wcode_array)
    print('orig_wcode_array')
    print(orig_wcode_array)
    print('dest_temperature_2m_max_array')
    print(dest_temperature_2m_max_array)
    print('orig_temperature_2m_max_array')
    print(orig_temperature_2m_max_array)
    print('dest_temperature_2m_min_array')
    print(dest_temperature_2m_min_array)
    print('orig_temperature_2m_min_array')
    print(orig_temperature_2m_min_array)
    print('dest_apparent_temperature_max_array')
    print(dest_apparent_temperature_max_array)
    print('orig_apparent_temperature_max_array')
    print(orig_apparent_temperature_max_array)
    print('dest_apparent_temperature_min_array')
    print(dest_apparent_temperature_min_array)
    print('orig_apparent_temperature_min_array')
    print(orig_apparent_temperature_min_array)
    print('dest_precipitation_hours_array')
    print(dest_precipitation_hours_array)
    print('orig_precipitation_hours_array')
    print(orig_precipitation_hours_array)
    print('dest_sunrise_array')
    print(dest_sunrise_array)
    print('orig_sunrise_array')
    print(orig_sunrise_array)
    print('dest_sunset_array')
    print(dest_sunset_array)
    print('orig_sunset_array')
    print(orig_sunset_array)
    print('dest_windspeed_10m_max_array')
    print(dest_windspeed_10m_max_array)
    print('orig_windspeed_10m_max_array')
    print(orig_windspeed_10m_max_array)
    print('dest_windgusts_10m_max_array')
    print(dest_windgusts_10m_max_array)
    print('orig_windgusts_10m_max_array')
    print(orig_windgusts_10m_max_array)
    print('dest_winddirection_10m_dominant_array')
    print(dest_winddirection_10m_dominant_array)
    print('orig_winddirection_10m_dominant_array')
    print(orig_winddirection_10m_dominant_array)


    #df1.to_csv('trimmed_merged_file_weather_fixed.csv', index=False)