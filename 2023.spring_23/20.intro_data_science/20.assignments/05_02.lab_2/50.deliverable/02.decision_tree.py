# May 01, 2023
# KNN Classification

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score, confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt
import os

# ============================================================
# 1 - Load a the dataset
# ============================================================
project_dir = os.path.dirname(__file__)
file = "02.data.csv"
file = project_dir + "/" + file
df = pd.read_csv(file)

# Segregate the inputs data from the label
col_label = 'Decision'
data = df.drop(columns=[col_label])
labels = df[col_label]
x_data = df.iloc[:, [1,2,3]].values
y_labels = df.iloc[:, 1].values

# ============================================================
# 2 - Train the model
# ============================================================
# split data to training set & testing sets. Then standardize the input
# data_train, data_val, labels_train, labels_val = train_test_split(data, labels, test_size = 0.4, random_state = 20)
data_train, data_val, labels_train, labels_val = train_test_split(x_data, y_labels, test_size = 0.4, random_state = 20)

# scaler = StandardScaler()
# data_train = scaler.fit_transform(data_train)
# data_val = scaler.transform(data_val)
# exit(0)

# Train the model
best_k = 5
decision_tree = DecisionTreeClassifier(criterion='entropy', random_state=0)
decision_tree.fit(data_train, labels_train) # TODO: This line have issue because of string values instead of int/float

# ============================================================
# 4 - Make prediction
# ============================================================
pred = decision_tree.predict(data_val)

print("Accuracy = {}%".format((sum(labels_val == pred) / labels_val.shape[0]) * 100))
print(df)

