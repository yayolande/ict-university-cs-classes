# May 07, 2023
# Support Vector Machine Lab 3

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm
import os

def show_diabetes_diagnostic(outcome):
    start_color = '\033[2;31;43m'
    end_color = '\033[0;0m'

    if outcome == 1:
        print(f'You are {start_color} diabetic {end_color}')
    elif outcome == 0:
        print(f'Good news, you are {start_color} healthy {end_color}')
    else:
        print('Waring, an unexpected diagnostic have been provided, check that the data are correct')

# ============================================================
# 1 - Load dataset
# ============================================================
project_dir = os.path.dirname(__file__)
os.chdir(project_dir)

file = '00.diabetes.csv'
fd = pd.read_csv(file)

# Output essential statical features about the dataset
output = fd.describe()
# output = fd['Outcome'].value_counts()
# output = fd.groupby('Outcome').mean()

# Separate Data/Inputs & Labels
X = fd.drop(columns=['Outcome'], axis=1).values
Y = fd['Outcome'].values

# Data Scaling
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# ============================================================
# 2 - Train the model
# ============================================================
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# ============================================================
# 3 - Predicting a sample data
# ============================================================
# Make Prediction & Verify model accuracy
# Training data prediction
train_pred = classifier.predict(X_train)
train_score_accuracy = accuracy_score(Y_train, train_pred)

# Testing data prediction
test_pred = classifier.predict(X_test)
test_score_accuracy = accuracy_score(Y_test, test_pred)

# ============================================================
# 4.a - single datum prediction (Easiest way)
# ============================================================
single_sample = [[1,85,66,29,0,26.6,0.351,31]]
expected_output = [0]
single_sample = scaler.transform(single_sample)

pred = classifier.predict(single_sample)
pred_accuracy = accuracy_score(expected_output, pred)

# ============================================================
# 4.b - single datum prediction (Boilerplate but recommended if possible)
# ============================================================
single_sample = [1,85,66,29,0,26.6,0.351,31]
expected_output = [0]
single_sample = np.asarray(single_sample)
single_sample = single_sample.reshape(1, -1)
single_sample = scaler.transform(single_sample)

pred = classifier.predict(single_sample)
pred_accuracy = accuracy_score(expected_output, pred)

# ============================================================
# 5 - Printing the Output
# ============================================================
# Print stuffs to the screen
# print(fd.head().to_string())
# print(X.head())
# print(Y.head())

# print(output)
print('==============================================')
print('==============================================')
print(f'Lab 3 - Support Vector Machine (ML)\n')
print('Training accuracy: ', train_score_accuracy)
print('Test accuracy score', test_score_accuracy)
print('Prediction accuracy score', pred_accuracy)

show_diabetes_diagnostic(pred_accuracy)
print('==============================================')
print('==============================================')

