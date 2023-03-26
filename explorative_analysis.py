import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data into a Pandas DataFrame
df = pd.read_csv('final_merged_file_categorized_outliers.csv')

# Group the data by a column of interest
grouped_data = df.groupby('ARRIVAL_DELAY_CATEGORY').size()

# Create a pie chart of the grouped data

plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%')
plt.show()



# Load the data into a Pandas DataFrame
df = pd.read_csv('final_merged_file_categorized.csv')

# Select the columns of interest
columns_of_interest = ['ARRIVAL_DELAY_CATEGORY', 'SCHEDULED_DEPARTURE', 'DESTINATION_WCODE', 'ORIGIN_WCODE' ,'SCHEDULED_ARRIVAL' ,'DESTINATION_PRECIPITATION_HOURS' ,'ORIGIN_PRECIPITATION_HOURS','DESTINATION_WINDGUSTS_10M_MAX' ,'ORIGIN_WINDGUSTS_10M_MAX' ,'ORIGIN_WINDSPEED_10M_MAX'  ,'DESTINATION_WINDSPEED_10M_MAX' ,'ORIGIN_WINDDIRECTION_10M_DOMINANT_10M_MAX' ,'ORIGIN_STATE' ,'DESTINATION_WINDDIRECTION_10M_DOMINANT_10M_MAX' ,'ORIGIN_TEMPERATURE_2M_MAX' ,'DESTINATION_TEMPERATURE_2M_MAX' ,'ORIGIN_AIRPORT_NAME' ,'DESTINATION_APPARENT_TEMPERATURE_MAX' ,'DAY' ,'FIRST_FLIGHT' ,'MONTH' ,'TYPE']

# Create a correlation matrix of the selected columns
corr_matrix = df[columns_of_interest].corr()

# Create a heatmap of the correlation matrix
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')

# Show the plot
plt.show()