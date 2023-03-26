import pandas as pd

df = pd.read_csv('final_merged_file_categorized.csv')

target_array = []

for index, row in df.iterrows():
    if row['ARRIVAL_DELAY'] <= 0:
        target_array.append(-1)
    elif row['ARRIVAL_DELAY'] <= 15:
        target_array.append(0)
    elif 15 < row['ARRIVAL_DELAY'] < 60:
        target_array.append(1)
    else:
        target_array.append(2)

df['ARRIVAL_DELAY_CATEGORY_4'] = target_array
df.to_csv('final_merged_file_categorized_with_4_categories.csv', index=False)
