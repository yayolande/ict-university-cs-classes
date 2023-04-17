# April 17, 2023
# Create a Data Frame

import pandas as pd

data = {
    "Gender": ['M', 'M', 'F', 'F', 'F'],
    "Age": [45, 12, 30, 28, 19],
}

df = pd.DataFrame(data)

print(df.to_string())