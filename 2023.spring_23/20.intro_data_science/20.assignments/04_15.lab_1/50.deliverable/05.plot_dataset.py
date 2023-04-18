# April 18, 2023
# Plot Dataset

import pandas as pd
import matplotlib.pyplot as plt

file = '05.data.csv'
df = pd.read_csv(file)

# df = df.sort_values(by = "Weight", ascending = False)
# df.plot(kind = 'area', stacked = False, figsize=(10, 4))
df.plot(kind = 'line', xlabel = 'Index', ylabel = 'Values')
plt.show()

# print(df.to_string())
# print(df.corr())
# exit(0)