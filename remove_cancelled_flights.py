import numpy
import pandas as pd

df = pd.read_csv('merged_file.csv')

df = df[~numpy.isnan(df["DEPARTURE_DELAY"])]

df.to_csv("merged_file_removed_cancelled.csv", index=False)