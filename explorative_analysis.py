import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data into a Pandas DataFrame
df = pd.read_csv('final_merged_file_categorized_outliers_with_delay.csv')

# Group the data by a column of interest
grouped_data = df.groupby('ARRIVAL_DELAY_CATEGORY').size()

# Create a pie chart of the grouped data

plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%')
plt.show()

# Group the data by a column of interest
grouped_data = df.groupby('DAY_OF_WEEK').size()

# Create a pie chart of the grouped data

plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%')
plt.show()

grouped_data = df.groupby('MONTH').size()

# Create a pie chart of the grouped data

plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%')
plt.show()

# Load the data into a Pandas DataFrame
df = pd.read_csv('final_merged_file_categorized_outliers.csv')

# Select the columns of interest
columns_of_interest = ['ARRIVAL_DELAY_CATEGORY', 'SCHEDULED_DEPARTURE', 'DESTINATION_WCODE', 'ORIGIN_WCODE' ,'SCHEDULED_ARRIVAL' ,'DESTINATION_PRECIPITATION_HOURS' ,'ORIGIN_PRECIPITATION_HOURS','DESTINATION_WINDGUSTS_10M_MAX' ,'ORIGIN_WINDGUSTS_10M_MAX' ,'ORIGIN_WINDSPEED_10M_MAX'  ,'DESTINATION_WINDSPEED_10M_MAX' ,'ORIGIN_WINDDIRECTION_10M_DOMINANT_10M_MAX' ,'ORIGIN_STATE' ,'DESTINATION_WINDDIRECTION_10M_DOMINANT_10M_MAX' ,'ORIGIN_TEMPERATURE_2M_MAX' ,'DESTINATION_TEMPERATURE_2M_MAX' ,'ORIGIN_AIRPORT_NAME' ,'DESTINATION_APPARENT_TEMPERATURE_MAX','FIRST_FLIGHT', 'AIRLINE', 'MONTH' ,'TYPE']
#columns_of_interest = ['ARRIVAL_DELAY_CATEGORY', 'ARRIVAL_DELAY', 'DEPARTURE_DELAY', 'AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY' ,'AIR_SYSTEM_DELAY','DEPARTURE_TIME' ,'WHEELS_OFF' ,'TAXI_OUT']
# columns_of_interest = df.columns
# columns_of_interest = columns_of_interest.delete(columns_of_interest.get_loc('CANCELLATION_REASON'))
# columns_of_interest = columns_of_interest.delete(columns_of_interest.get_loc('ORIGIN_COUNTRY'))
# columns_of_interest = columns_of_interest.delete(columns_of_interest.get_loc('DESTINATION_COUNTRY'))
# columns_of_interest = columns_of_interest.delete(columns_of_interest.get_loc('YEAR'))
# columns_of_interest = columns_of_interest.delete(columns_of_interest.get_loc('CANCELLED'))

# Create a correlation matrix of the selected columns
corr_matrix = df[columns_of_interest].corr()

# Create a heatmap of the correlation matrix
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')

# Show the plot
plt.show()

# Assuming your dataset is stored in a pandas dataframe called 'flights'
flight_counts = df.groupby(['MONTH', 'ARRIVAL_DELAY_CATEGORY']).size().reset_index(name='count')

# Pivot the data to create separate columns for each flight category
flight_counts_pivot = flight_counts.pivot(index='MONTH', columns='ARRIVAL_DELAY_CATEGORY', values='count')

# Create a line graph for the flight counts by month and category
flight_counts_pivot.plot.line()
plt.xlabel('Month')
plt.ylabel('Number of flights')
plt.title('Flight counts by month and flight arrival category')
plt.show()

# Read CSV into pandas
df1 = pd.read_csv('final_merged_file_categorized_with_4_categories.csv')

# # Group the data by a column of interest
# grouped_data1 = df1.groupby('SEASON').size()
#
# # Create a pie chart of the grouped data
#
# plt.pie(grouped_data1, labels=grouped_data1.index, autopct='%1.1f%%')
# plt.show()

grouped_data1 = df1.groupby('AIRLINE').size()

# Create a pie chart of the grouped data
df = pd.read_csv('final_merged_file_categorized_outliers_with_delay.csv')

plt.pie(grouped_data1, labels=grouped_data1.index, autopct='%1.1f%%')
plt.show()

df['TYPE'].value_counts().plot(kind='bar');
plt.show()

sns.countplot(df['DAY_OF_WEEK'])
plt.title('Total Athletes contribution in summer olympics over time')
plt.xlabel('Years')
plt.ylabel('No. of Athlete')
