# May 07, 2023
# Apriori (Machine Learning)
# Find String Association rules among items
# Given min support = 40% & min confidence level = 70%

import pandas as pd
from apyori import apriori
import os

project_dir = os.path.dirname(__file__)
os.chdir(project_dir)

file = "02.data.csv"
fd = pd.read_csv(file, header=None)
fd.dropna(inplace=True, how='all', axis=1)

min_support = .20
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

final_rules = apriori(items, min_support=min_support, min_confidence=min_confidence, min_lift=min_lift, min_length=min_length)
# final_rules = apriori(items, min_support=min_support, min_confidence=min_confidence)
final_results = list(final_rules)

print(final_results)