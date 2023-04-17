# April 17, 2023
# Read and print the CSV file "data.csv"

import pandas as pd

file = "03.data.csv"
df = pd.read_csv(file)

print(df.to_string())