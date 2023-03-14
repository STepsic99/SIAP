import numpy
import pandas as pd

df = pd.read_csv('merged_file.csv')

df = df[~numpy.isnan(df["DEPARTURE_DELAY"])]

#df = df[not numpy.isnan(df.DEPARTURE_DELAY)]
# cnt = 0
# for index, row in df.iterrows():
#     if numpy.isnan(row['DEPARTURE_DELAY']):
#         print(index)
#         df.loc[index, 'DEPARTURE_DELAY'] = 'X'
#         cnt += 1

df.to_csv("merged_file_removed_cancelled.csv", index=False)