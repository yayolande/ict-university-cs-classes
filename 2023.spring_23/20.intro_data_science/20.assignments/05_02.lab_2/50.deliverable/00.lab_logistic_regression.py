# May 01, 2023
# Lab Logistic Regression

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os

def show_diabetes_diagnostic(outcome):
    start_color = '\033[2;31;43m'
    end_color = '\033[0;0m'

    if outcome == 1:
        print(f'You have an {start_color} Heart Disease {end_color}')
    elif outcome == 0:
        print(f'Good news, you are {start_color} healthy {end_color}')
    else:
        print('Waring, an unexpected diagnostic have been provided, check that the data are correct')

# ============================================================
# 1 - Load a the dataset
# ============================================================
project_dir = os.path.dirname(__file__)
os.chdir(project_dir)

file = "00.data.csv"
fd = pd.read_csv(file)

X = fd.drop(columns=['target'], axis=1).values
Y = fd['target'].values

# ============================================================
# 2 - Train the model
# ============================================================
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
model = LogisticRegression(max_iter=10000)
model.fit(X_train, Y_train)

# ============================================================
# 3 - Test the Model Accuracy
# ============================================================
pred_train = model.predict(X_train)
train_accuracy_score = accuracy_score(Y_train, pred_train)

pred_test = model.predict(X_test)
test_accuracy_score = accuracy_score(Y_test, pred_test)

# ============================================================
# 4 - Predicting a sample data
# ============================================================
single_sample = [[52,1,2,172,199,1,1,162,0,0.5,2,0,3]]
expected_output = [1]

pred = model.predict(single_sample)
pred_accuracy = accuracy_score(expected_output, pred)

# ============================================================
# 5 - Printing the Output
# ============================================================
print('==============================================')
print('==============================================')
print(f'Lab 2 - Logistic Regression (ML)\n')
print('Train accuracy score : ', train_accuracy_score)
print('Test accuracy score : ', test_accuracy_score)
print('Prediction accuracy score : ', pred_accuracy)

show_diabetes_diagnostic(pred_accuracy)
print('==============================================')
print('==============================================')

# print(fd.info())
# print(fd.describe())
# print(fd.to_string())

