import pandas as pd
df = pd.read_csv('trimmed_merged_file_scrapped_cleaned.csv', encoding="ISO-8859-1")
df.drop_duplicates(subset=["TAIL_NUMBER"], inplace=True)
df.to_csv('trimmed_merged_file_scrapped_cleaned_no_2.csv', index=False)

