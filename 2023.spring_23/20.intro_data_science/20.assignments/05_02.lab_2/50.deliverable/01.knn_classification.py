# May 01, 2023
# KNN Classification

import pandas as pd
import pathlib as path
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import neighbors
from sklearn.metrics import f1_score, confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt

# file_path = os.path.dirname(__file__)
# file_path = file_path + "/here_we_go.txt"
# print(file_path)
# print(__file__)
# exit(0)

# Load file data
project_dir = os.path.dirname(__file__)
file = "01.data.csv"
file = project_dir + "/" + file

df = pd.read_csv(file)
# df = pd.read_csv(file, index_col = 0)

# Segregate the inputs data from the label
col_label = 'species'
data = df.drop(columns=[col_label])
labels = df[col_label]
data_to_predict = [[5.2, 2.4]]
label_predicted = []

# split data to training set & testing sets. Then standardize the input
data_train, data_val, labels_train, labels_val = train_test_split(data, labels, test_size = 0.2, stratify = labels, random_state = 20)

scaler = StandardScaler()
data_train = scaler.fit_transform(data_train)
data_val = scaler.transform(data_val)
# exit(0)

# Train the model
best_k = 5
KNN_model = neighbors.KNeighborsClassifier(n_neighbors=best_k, n_jobs=-1)
KNN_model.fit(data_train, labels_train)

# Make prediction
pred = KNN_model.predict(data_val)

# Plot F1-Score relationship to K with some calculation made in advance
f1_list = []
k_list = []
for k in range(1, 12):
    clf = neighbors.KNeighborsClassifier(n_neighbors=k, n_jobs=-1)
    clf.fit(data_train, labels_train)
    pred_1 = clf.predict(data_val)
    f = f1_score(labels_val, pred_1, average = 'macro')
    f1_list.append(f)
    k_list.append(k)

plt.plot(k_list, f1_list)
plt.xlabel('Number of Neighbours, K')
plt.ylabel('F1-Score')
plt.title('Graph to get an overview of the K value accuracy')
# plt.show()

# Prediction the species
label_predicted = KNN_model.predict(data_to_predict)

# print(df.to_string())
# print(data.to_string())
# print(labels.to_string())
# print("Accuracy = {}%".format((sum(labels_val == pred) / labels_val.shape[0]) * 100))
print(f'Prediction: [{data_to_predict[0][0]}, {data_to_predict[0][1]}] ---> {label_predicted[0]}')

