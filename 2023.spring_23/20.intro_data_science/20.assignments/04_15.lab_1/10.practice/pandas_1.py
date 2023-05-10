# This practice session follow a data science tutorial found on W3Schools
# https://www.w3schools.com/python/pandas/default.asp

import pandas
import pandas as pd

dataset = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}

# myvar = pandas.DataFrame(dataset)
myvar = pd.DataFrame(dataset) # Multi-dimensional table (DataFrame)

print(myvar)
print(pd.__version__)
# exit(0)

#------------------------------------------------------------------
# v0.2.0 --- Pandas Series
#------------------------------------------------------------------
# A Pandas 'Series' is similar to a table row. Advance forward to learn more

print("\n ----------- \n")

a = [7, 3, 5]
calories = {
    "day1": 420,
    "day2": 380,
    "day3": 200,
}

data = {
    "calories": [420, 380, 270],
    "duration": [45, 30, 40],
}

series = pd.Series(a) # a pandas series is like a column in a table
series = pd.Series(a, index = ["x", "y", "z"]) # use 'index' to give label to each row
series_v2 = pd.Series(calories)
series_v2 = pd.Series(calories, index = ["day1", "day2"]) # Only show day 1 & 2 series
table = pd.DataFrame(data, index = ["Steve", "Hakimi", "CR 7"])

# print(table.index)
# exit(0)

print (series)
print (series[0])
print (series['x'])
print(series_v2)
print(table)


#------------------------------------------------------------------
# v0.3.0 --- Pandas DataFrame
#------------------------------------------------------------------
# Pandas 'DataFrame' is a 2 dimensional data structure, 
# like a 2 dimensional array, or a table with rows and columns
print("\n ----------- \n")

data = {
    "calories": [420, 380, 270],
    "duration": [45, 30, 40],
}

table = pd.DataFrame(data)
table_2 = pd.DataFrame(data, index = ["day1", "day2", "day3"]) # Per default, for each row, label are indexed from '0' and incremented by one for each row
# However, when using 'index = [...]', we are overriding the default values by a custom ones

import os

project_dir = os.path.dirname(__file__)
os.chdir(project_dir)

# project_dir = project_dir + "/"
project_dir = ""
file_csv = project_dir + "data.csv"
tableCsv = pd.read_csv(file_csv)

print(table.loc[0]) # This return a pandas 'series' for row '0'
print(table.loc[[0, 1]]) # This return a pandas 'dataFrame' for row '0' and '1'
print(table.loc[0:2]) # This return a pandas 'dataFrame' for row '0, 1, 2'. It uses the python slice's feature

# print(table_2.loc[0])  # Dont use this, it trigger an exception since the label changed from '0' to 'day1'
print(table_2.loc["day1"]) # Return a Pandas 'series'
print(table_2.loc["day1":"day3"]) # Return a Pandas 'DataFrame'
print(tableCsv.loc[164])
print(tableCsv.to_string()) # Display all the rows, since pandas put a cap for long table
print(pd.options.display.max_rows) # Display the cutoff threshold for row items to display

#------------------------------------------------------------------
# v0.4.0 --- Analyzing DataFrame
#------------------------------------------------------------------

file_csv = project_dir + "data.csv"
pf = pd.read_csv(file_csv)
print(pf.head(10)) # similar than "head" cli, only show first items in table (header included)
print(pf.tail())
print(pf.info()) # give info about the dataset columns (count, data types, names, ...)

#------------------------------------------------------------------
# v0.5.0 --- Cleaning Data
#------------------------------------------------------------------
# Data cleaning means fixing bad data in your data set
# Bad data could be : Empty Cells, Data in Wrong Format, Wrong Data, Duplicate

# file = open('data.csv', 'r')
# print(file.read())
# file.close()

file_date_data = project_dir + "data_v2.csv"
table = pd.read_csv(file_date_data)
table.dropna(inplace = True)

tableReplace = pd.read_csv(file_date_data)
tableReplace.fillna(130, inplace = True) # Replace empty cell value by '130'

tableReplace = pd.read_csv(file_date_data)
tableReplace["Calories"].fillna(666, inplace = True) # Replace only for column 'Calories'

tableReplace = pd.read_csv(file_date_data)
mean = tableReplace["Calories"].mean()
median = tableReplace["Calories"].median()
mode = tableReplace["Calories"].mode()

tableReplace["Calories"].fillna(mean, inplace = True)
tableReplace["Calories"].fillna(median, inplace = True)
tableReplace["Calories"].fillna(mode[0], inplace = True)

print(table.to_string())
print(tableReplace.to_string())
print(mean)
# print(tableReplace.dtypes)


#------------------------------------------------------------------
# v0.6.0 --- Cleaning Data (Wrong Format)
#------------------------------------------------------------------

file_date_data = project_dir + "data_v2.csv"
table = pd.read_csv(file_date_data)
table['Date'] = pd.to_datetime(table['Date'], errors = 'coerce')
table.dropna(subset = ['Date'], inplace = True)

print(table.to_string())

#------------------------------------------------------------------
# v0.6.0 --- Cleaning Data (Wrong & Duplicated Data)
#------------------------------------------------------------------

file_date_data = project_dir + "data_v2.csv"
table = pd.read_csv(file_date_data)
table.loc[7, 'Duration'] = 45

df = pd.read_csv(file_date_data)
for x in df.index:
    if df.loc[x, 'Duration'] > 40:
        df.loc[x, 'Duration'] = 80
        df.drop(labels = [x], inplace = True)   # Drop a row with the specified labels
        # df.drop(x, inplace = True) # This version works as well

# df.drop(labels = [1, 2, 3], inplace = True)
table.drop_duplicates(inplace = True)

print(table.head(10).to_string())
print(df.to_string())
print(table.duplicated()) # print every row followed by whether it is duplicated row or not (True & False)
print(table.to_string())

#------------------------------------------------------------------
# v0.6.0 --- Correlation & Plot
#------------------------------------------------------------------

import matplotlib.pyplot as plt

table = pd.read_csv(file_csv)

# print(table.corr())
print(table.corr(numeric_only = True))

# table.plot()
# table.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
# table.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
table['Duration'].plot(kind = 'hist')
plt.show()

