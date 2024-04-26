# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:34:21 2024

@author: vahed
"""

from utils import *
from Kpca import kPCA
from pca import PCA

import pandas as pd
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
from pyod.models.ocsvm import OCSVM
from scipy.linalg import eigh
from sklearn.datasets import fetch_openml

# methods = ['kPCA','PCA','ParzenWindow','OCSVM']

# # Replace 'delimiter_here' with '\t' if your file is tab-delimited, or ' ' if it is space-delimited
# df = pd.read_csv('test sets/square.csv', delim_whitespace=True, header=None, names=['x', 'y'])

# # Display the first few rows to verify it looks correct
# print(df.head())

# from sklearn.model_selection import train_test_split

# # Assuming df_named_columns is your dataset loaded into a pandas DataFrame
# X = df[['x', 'y']]  # Features
# # If you had a target variable, it would be something like y = df['target']

# # Split the dataset into training and testing sets
# X_train, X_test, Y_train, Y_test = train_test_split(df['x'], df['y'], test_size=0.2, random_state=42)

# # X_train and X_eval are now your training and evaluation sets
# x_train=X_train.to_numpy()
# x_test=X_test.to_numpy()
# y_train=Y_train.to_numpy()
# y_test=Y_test.to_numpy()


# test_size = x_test.shape[0]
# idx = np.random.randint(0,test_size, int(test_size/2))
# x_val = x_test[idx]
# y_val = y_test[idx]
# x_test = x_test[~idx]
# y_test = y_test[~idx]

# X_train, X_test, _, _ = train_test_split(X, X, test_size=0.2, random_state=42)

from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
breast_cancer = fetch_ucirepo(id=14) 
  
# data (as pandas dataframes) 
X = breast_cancer.data.features 
y = breast_cancer.data.targets 
  
# metadata 
print(breast_cancer.metadata) 
  
# variable information 
print(breast_cancer.variables) 