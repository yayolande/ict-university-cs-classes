# April 17, 2023
# Import "data.csv" and perform data cleaning/cleansing

import pandas as pd
pd.options.display.max_rows = 999

file = "04.data.csv"
df = pd.read_csv(file)

df.drop_duplicates(inplace = True)

print(df.to_string())
print(df[df == 'NaN'])
# print(df['Pulse'] > 150)
# print(df[df['Pulse'] > 150])
# print(df[['Duration', 'Pulse']])
# print(df.duplicated())