import pandas as pd

df = pd.read_csv('final_merged_file_categorized_outliers_with_delay.csv')

target_array = []

for index, row in df.iterrows():
    if (row['MONTH'] == 3 and row['DAY_OF_WEEK'] >= 20) or (row['MONTH'] == 4) \
            or (row['MONTH'] == 5) or (row['MONTH'] == 6 and row['DAY_OF_WEEK'] <= 21):
        target_array.append(0)
    elif (row['MONTH'] == 6 and row['DAY_OF_WEEK'] > 21) or (row['MONTH'] == 7) \
            or (row['MONTH'] == 8) or (row['MONTH'] == 9 and row['DAY_OF_WEEK'] <= 23):
        target_array.append(1)
    elif (row['MONTH'] == 9 and row['DAY_OF_WEEK'] > 23) or (row['MONTH'] == 10) \
            or (row['MONTH'] == 11) or (row['MONTH'] == 12 and row['DAY_OF_WEEK'] <= 22):
        target_array.append(2)
    else:
        target_array.append(3)

df['SEASON'] = target_array
df.to_csv('final_merged_file_categorized_season_delay.csv', index=False)