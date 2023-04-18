# April 17, 2023
# Import "data.csv" and perform data cleaning/cleansing
# Note: No need to Clean Wrongly formatted data & Wrong Data
# Since there is none

import pandas as pd
pd.options.display.max_rows = 999

file = "04.data.csv"
df = pd.read_csv(file)

df.dropna(inplace = True)
df.drop_duplicates(inplace = True)

print(df.to_string())

# ---------------------------------
# Experimental
# ---------------------------------

# sum = 0
# for x in df.columns:
#     print(f'column : {x}\n')
#     df = df[df[x] > 130]
#     sum = sum + df

# df = df[df['Pulse'] > 130]
# df = df[df['Duration'] > 30]

# df = df [(df['Calories'].isna())] # DataFrame only containing rows with at least one 'NaN' in their cell
# df = df.isna()

# print(sum.to_string())
# print(df[df == 'NaN'])
# print(df['Pulse'] > 150)
# print(df[df['Pulse'] > 150])
# print(df[['Duration', 'Pulse']])
# print(df.duplicated())

# print(df['Calories'].max())
# print(df['Pulse'].max())
# print(df['Duration'].max())