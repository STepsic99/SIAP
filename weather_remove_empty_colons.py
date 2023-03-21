import pandas as pd
import numpy

df = pd.read_csv('trimmed_merged_file_scrapped.csv', encoding="ISO-8859-1")

# for index, row in df.iterrows():
#     print(row['TYPE'])

#df = df1[df1["TYPE"]]

df = df[~pd.isna(df["TYPE"]) & ~pd.isna(df["FIRST_FLIGHT"])]

df.to_csv("trimmed_merged_file_scrapped_cleaned.csv", index=False)
