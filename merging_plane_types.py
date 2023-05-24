import pandas as pd

df = pd.read_csv('final_merged_file_categorized_outliers.csv')

hash_map = {}

for index, row in df.iterrows():
    value = hash_map.get(row['TYPE'], 0)
    if value == 0:
        hash_map[row['TYPE']] = 1
    else:
        hash_map[row['TYPE']] += 1

to_be_removed = []
for key,value in hash_map.items():
    if value < 10:
        to_be_removed.append(key)

to_be_removed.sort()

target_array = []

for index, row in df.iterrows():
    if row['TYPE'] in to_be_removed:
        target_array.append(int(to_be_removed[0]))
    else:
        target_array.append(int(row['TYPE']))

df['TYPE_MERGED'] = target_array
df.to_csv('final_merged_file_categorized_outliers_type.csv', index=False)