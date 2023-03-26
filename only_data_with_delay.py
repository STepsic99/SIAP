import pandas as pd

df = pd.read_csv('final_merged_file_categorized.csv')

df = df[df['ARRIVAL_DELAY'] > 0]

df.to_csv('final_merged_file_categorized_outliers_with_delay.csv', index=False)