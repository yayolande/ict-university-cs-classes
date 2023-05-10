# May 07, 2023
# Apriori (Machine Learning)
# Find String Association rules among items
# Given min support = 40% & min confidence level = 70%

import pandas as pd
from efficient_apriori import apriori
import os

project_dir = os.path.dirname(__file__)
os.chdir(project_dir)

file = "02.data.csv"
fd = pd.read_csv(file, header=None)
fd.dropna(inplace=True, how='all', axis=1)

min_support = .01
min_confidence = .7
min_length = 2
min_lift = 5

items = []
fd_row_count = fd.shape[0]
fd_col_count = fd.shape[1]

for i in range(fd_row_count):
    # fd.value_counts()
    items.append([str(fd.values[i, j]) for j in range(fd_col_count) if str(fd.values[i, j]) != 'nan'])
    pass

itemsets, rules = apriori(items, min_support=min_support, min_confidence=min_confidence)

# print(rules)
print(*rules, sep="\n")
