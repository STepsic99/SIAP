import numpy
import pandas as pd

df = pd.read_csv('flightsFull.csv')
for index, row in df.iterrows():
    if numpy.isnan(row['DEPARTURE_DELAY']):
        print(index)
        df.loc[index, 'DEPARTURE_DELAY'] = 'X'

df.to_csv("flightsFullWithFixedTarget.csv", index=False)