# from bs4 import BeautifulSoup
# from selenium import webdriver


################################################MergingFiles
import pandas as pd
import historical_weather_data
from shapely.geometry import Point, LineString
import math
import datetime
from shapely.ops import split

# # read the two csv files into dataframes
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

################################################MergingFiles

historical_weather_data.add_weather()



