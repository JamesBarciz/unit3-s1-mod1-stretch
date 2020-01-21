# DISCLAIMER:
# This script contains various functions that were used in class
# And could be used in future assignments

# 1. train_test_wrangle:
# Wrangles a CLEANED dataframe into Train, Val, Test
# arguments:
# A. data - splits into train, val, test and its corresponding X & y Matrices
# B. target - desired target column which must be within quotes

from sklearn.model_selection import train_test_split
from sklearn.utils.multiclass import unique_labels
from sklearn.metrics import confusion_matrix
import seaborn as sns
import pandas as pd


def train_test_wrangle(data, target):
    # Train 80% / Test 20%
    train, test = train_test_split(data, train_size=0.8,
                                   test_size=0.2, random_state=42
                                   )
    # Train 75% / Val 25% (default)
    train, val = train_test_split(train, train_size=0.75,
                                  test_size=0.25, random_state=42
                                  )

    X_train = train.drop(columns=target)
    y_train = train[target]
    X_val = val.drop(columns=target)
    y_val = val[target]
    X_test = test.drop(columns=target)

    return X_train, y_train, X_val, y_val, X_test

# 2. plot_confusion_matrix:
# Confusion Matrix visualization with seaborn.heatmap
# arguments:
# A. y_true = (y_train or y_val)
# B. y_pred - predicted values in a y matrix


def plot_confusion_matrix(y_true, y_pred):
    labels = unique_labels(y_true)
    columns = [f'Predicted {label}' for label in labels]
    index = [f'Actual {label}' for label in labels]
    df = pd.DataFrame(confusion_matrix(y_true, y_pred),
                      columns=columns, index=index
                      )
    return sns.heatmap(df, annot=True, fmt='d', cmap='Blues')
