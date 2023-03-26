# from bs4 import BeautifulSoup
# from selenium import webdriver


################################################MergingFiles
import pandas as pd

import historical_weather_data
from shapely.geometry import Point, LineString
import math
import datetime
from shapely.ops import split

# read the two csv files into dataframes
# df1 = pd.read_csv('flightsFull.csv')
# df2 = pd.read_csv('orgin_airports.csv')
# df3 = pd.read_csv('destination_airports.csv')
#
# # merge the dataframes based on the common column
# merged_df = pd.merge(df1, df2, on='ORIGIN_AIRPORT')
#
# # write the merged dataframe to a new csv file
# merged_df.to_csv('merged_file_origin.csv', index=False)
#
# df4 = pd.read_csv('merged_file_origin.csv')
#
# merged_df2 = pd.merge(df3, df4, on='DESTINATION_AIRPORT')
#
# merged_df2.to_csv('merged_file.csv', index=False)
#
# print('finish_merge')

################################################historical api

#historical_weather_data.add_weather()

################################################Merging weather and scraped files
# df1 = pd.read_csv('trimmed_merged_file_scrapped_cleaned_no_2.csv')
# df2 = pd.read_csv('trimmed_merged_file_weather.csv')
# merged_df = pd.merge(df1, df2, on='TAIL_NUMBER')
# merged_df.to_csv('final_merged_file.csv', index=False)
#######################################################corelation

df = pd.read_csv('final_merged_file_categorized.csv')
types_array = df.dtypes
hash_map = {}
cnt1 = 0
for col in df.columns:
    if types_array[col] == 'object':
        df[col]=df[col].astype('category').cat.codes
    corr=df[col].corr(df['ARRIVAL_DELAY'])
    hash_map[col] = abs(corr)
#    print(str(corr) + " " + col)

##################################################HashMap

sorted_hash_map = sorted(hash_map.items(), key=lambda x: x[1])

for x in sorted_hash_map:
    print(x)
print(sorted_hash_map)







########################################################

# import numpy as n
# import matplotlib. pyplot as pt
# var1 = pd. Series (df['DELAY_CATEGORY'])
# var2 = pd. Series (df['ORIGIN_WCODE'])
# pt. scatter (var1, var2)
# pt. plot (n. unique (var1), n. poly1d (n. polyfit (var1, var2, 1))(n. unique (var1)), color = 'green')
# pt. show()