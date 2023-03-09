# import pandas as pd
# from geopy.geocoders import Nominatim
#
# # create a geolocator object
# geolocator = Nominatim(user_agent="http")
#
# # load the dataset
# df = pd.read_csv('ged_summary.csv')
#
# # define a function to get the latitude and longitude for a city
# def get_coords(city):
#     location = geolocator.geocode(city)
#     if location:
#         return location.latitude, location.longitude
#     else:
#         return None, None
#
# # add latitude and longitude columns to the dataset
# # df['OriginLatitude'], df['OriginLongitude'] = zip(*df['OriginCityName'].apply(get_coords))
# # df['DestLatitude'], df['DestLongitude'] = zip(*df['DestCityName'].apply(get_coords))
#
# df['latitude'], df['longitude'] = zip(*df['country'].apply(get_coords))
#
# # save the updated dataset
# df.to_csv('ged_summary_with_coords.csv', index=False)

################################################MergingFiles
import pandas as pd
from shapely.geometry import Point, LineString
import math
import datetime
from shapely.ops import split

# # read the two csv files into dataframes
# df1 = pd.read_csv('flights.csv')
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

################################################MergingFiles
def check_coords_in_radius(coords1, coords2, radius):
    # coords1 and coords2 are tuples of latitude and longitude
    lat1, lon1 = coords1
    lat2, lon2 = coords2
    # Radius of the earth in kilometers
    R = 6371
    # Convert latitude and longitude to radians
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    # Calculate the Haversine formula
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    # Check if the distance is within the specified radius
    if distance <= radius:
        return True
    else:
        return False

def check_for_intersection(city_lat, city_lng, radius, orgin_airport_lat, orgin_airport_lon, dest_airport_lat, dest_airport_lon):

    # Define the line segment
    line_coords = [(orgin_airport_lon, orgin_airport_lat), (dest_airport_lon, dest_airport_lat)]
    line = LineString(line_coords)

    if check_coords_in_radius((orgin_airport_lat, orgin_airport_lon), (city_lat, city_lng), radius):
        return True

    return check_coords_in_radius((dest_airport_lat, dest_airport_lon), (city_lat, city_lng), radius)



df1 = pd.read_csv('USAterrorismdb_0616dist.csv', encoding="ISO-8859-1")
intersect_array = []
city_inter_array = []
df2 = pd.read_csv('merged_file.csv')
for index, row in df2.iterrows():
    for index1, row1 in df1.iterrows():
        flight_date = datetime.datetime(row['YEAR'], row['MONTH'], row['DAY'])
        attack_date = datetime.datetime(row1['iyear'], row1['imonth'], row1['iday'])
        attack_date_end = attack_date + datetime.timedelta(days=10)
        attack_date_start = attack_date - datetime.timedelta(days=10)
        intersects = check_for_intersection(row1['latitude'], row1['longitude'], 100, row['ORIGIN_LATITUDE'], row['ORIGIN_LONGITUDE'], row['DESTINATION_LATITUDE'], row['DESTINATION_LONGITUDE'])
        if intersects and attack_date_start < flight_date < attack_date_end:
            intersect_array.append(1)
            city_inter_array.append(row1['city'])
            break
        else:
            if index1 == 37:
                intersect_array.append(0)
                city_inter_array.append('')

df2['armed_conflicts_affected'] = intersect_array
df2['conflict_city'] = city_inter_array
df2.to_csv('merged_file_conflicts_flights.csv', index=False)



