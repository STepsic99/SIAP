from scipy import stats
import numpy as np
import pandas as pd

df = pd.read_csv('final_merged_file_categorized_outliers.csv')

data = np.array(df['DESTINATION_WINDGUSTS_10M_MAX'])

z_scores = stats.zscore(data)
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3)
new_data = data[filtered_entries]
print(np.sort(new_data)) # [1 2 3 4]
new_data_sorted = np.sort(new_data)


df = df[(df["DESTINATION_WINDGUSTS_10M_MAX"] >= new_data_sorted[0]) & (df["DESTINATION_WINDGUSTS_10M_MAX"] <= new_data_sorted[-1])]

df.to_csv('final_merged_file_categorized_outliers.csv', index=False)