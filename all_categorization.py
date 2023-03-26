import pandas as pd
df = pd.read_csv('final_merged_file_categorized.csv')
types_array = df.dtypes
for col in df.columns:
    if types_array[col] == 'object':
        df[col]=df[col].astype('category').cat.codes
df.to_csv('final_merged_file_categorized.csv', index=False)
