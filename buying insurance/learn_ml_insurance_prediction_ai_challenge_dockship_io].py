# -*- coding: utf-8 -*-
"""[Learn ML Insurance Prediction  AI Challenge - Dockship.io]Peddi Anurag's_notebook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t0sadBSAu61X6-8yerNXOpVzNdQMu8oC

# Learn ML Insurance Prediction AI Challenge
"""

!wget -O "learn_ml_insurance_prediction__ai_challenge-dataset.zip" "https://dockship-job-models.s3.ap-south-1.amazonaws.com/196c328ad298ef1476f56437902688ef?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIDOPTEUZ2LEOQEGQ%2F20210123%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20210123T152508Z&X-Amz-Expires=1800&X-Amz-Signature=46f15505be2fdfbd69a35e98ba4ba3159efdacde48ca9d0ba7fcd1e719bb468c&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3D%22learn_ml_insurance_prediction__ai_challenge-dataset.zip%22"

# Commented out IPython magic to ensure Python compatibility.
# Required modules

import os
import numpy as np
import pandas as pd

from zipfile import ZipFile
from matplotlib import pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# %matplotlib inline
plt.rcParams['figure.figsize'] = (12, 7)

# Extract the dataset

with ZipFile('learn_ml_insurance_prediction__ai_challenge-dataset.zip', 'r') as zf:
    zf.extractall('./')

# Loading the dataset

train = pd.read_csv('TRAIN.csv')
train.head()

# Inspecting the data

train.info()
train.describe()

# Encoding some of the columns

train['Gender'].replace(train['Gender'].value_counts().index, [0, 1], inplace=True)
train['Vehicle_Age'].replace(train['Vehicle_Age'].value_counts().index, [0, 1, 2], inplace=True)
train['Vehicle_Damage'].replace(train['Vehicle_Damage'].value_counts().index, [0, 1], inplace=True)

# Separating out features and labels

X = train.loc[:, train.columns != 'Response']
y = train['Response']

# Train and Test Split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Fitting the model

model = LogisticRegression()
model.fit(X_train, y_train)

# Loading the test set

test = pd.read_csv('TEST.csv')
test.head()

# Encoding on the test data

test['Gender'].replace(test['Gender'].value_counts().index, [0, 1], inplace=True)
test['Vehicle_Age'].replace(test['Vehicle_Age'].value_counts().index, [0, 1, 2], inplace=True)
test['Vehicle_Damage'].replace(test['Vehicle_Damage'].value_counts().index, [0, 1], inplace=True)

# Predicting on the test set

pred = model.predict(test)

# Submission

output = pd.DataFrame({'id': test['id'], 'Response': pred})
output.to_csv('output.csv', index=False)

