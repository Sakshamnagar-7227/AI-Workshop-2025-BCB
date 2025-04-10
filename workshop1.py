# -*- coding: utf-8 -*-
"""Workshop1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1huJlC_KGn5z_vfI8yTi86cYQHaO59PFR
"""

# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Sample Dataset
from sklearn.datasets import load_iris

data = load_iris()
X = data.data
y = data.target

print("Feature Names:", data.feature_names)
print("Target Names:", data.target_names)

# Quick Look at Data
pd.DataFrame(X, columns=data.feature_names).head()

# Split the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. Train a Decision Tree Classifier
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

# Predict and Evaluate
dt_predictions = dt_model.predict(X_test)
print("\nDecision Tree Accuracy:", accuracy_score(y_test, dt_predictions))

# 2. Train a Logistic Regression Model
# (For simplicity, reduce to a binary classification problem)
# Let's classify if the flower is Setosa or not

binary_y = (y == 0).astype(int)  # Setosa = 1, Others = 0
X_train_bin, X_test_bin, y_train_bin, y_test_bin = train_test_split(X, binary_y, test_size=0.2, random_state=42)

lr_model = LogisticRegression(max_iter=200)
lr_model.fit(X_train_bin, y_train_bin)

# Predict and Evaluate
lr_predictions = lr_model.predict(X_test_bin)
print("\nLogistic Regression Accuracy:", accuracy_score(y_test_bin, lr_predictions))

# Confusion Matrix for Logistic Regression
cm = confusion_matrix(y_test_bin, lr_predictions)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

print("\nClassification Report:\n", classification_report(y_test_bin, lr_predictions))