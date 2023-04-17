# April 16, 2023
# Create an index series

import pandas as pd

data = {
    'a': 10,
    'b': 15,
    'c': 18,
    'd': 17,
    'e': 20,
}

series = pd.Series(data)

print(series.to_string())
