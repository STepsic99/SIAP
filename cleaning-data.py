import pandas as pd

df = pd.read_csv('merged_file_removed_cancelled.csv', encoding="ISO-8859-1")

df.sort_values(by='DEPARTURE_DELAY', ascending=True)

df[::500].to_csv('trimmed_merged_file.csv', index=False)


