import time

import pandas as pd
import requests

df1 = pd.read_csv('merged_file_conflicts_flights.csv', encoding="ISO-8859-1")
dest_wcode_array = []
orig_wcode_array = []
for index, row in df1.iterrows():
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
                         "&end_date=" + str(row['YEAR']) + "-" + month + "-" + day + "&daily=weathercode&&timezone=America/Anchorage")
            r2 = requests.get("https://archive-api.open-meteo.com/v1/archive?latitude=" + str(row['ORIGIN_LATITUDE']) +
                          "&longitude=" + str(row['ORIGIN_LONGITUDE']) + "&start_date=" +
                          str(row['YEAR']) + "-" + month + "-" + day +
                          "&end_date=" + str(row['YEAR']) + "-" + month + "-" + day + "&daily=weathercode&&timezone=America/Anchorage")
            num = 1
        except:
            time.sleep(5)

    data1 = r1.json()
    data2 = r2.json()
    print(data1['daily']['weathercode'][0])
    dest_wcode_array.append(data1['daily']['weathercode'][0])
    orig_wcode_array.append(data2['daily']['weathercode'][0])

df1['DESTINATION_WCODE'] = dest_wcode_array
df1['ORIGIN_WCODE'] = orig_wcode_array
df1.to_csv('merged_file_conflicts_flights_weather.csv', index=False)