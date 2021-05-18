
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE



from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score, precision_score, plot_confusion_matrix
from sklearn.metrics import f1_score

from scipy.special import boxcox1p
from scipy.stats import boxcox_normmax
from scipy.stats import skew, boxcox
from sklearn import preprocessing


# On load le model logreg
loaded_model = pickle.load(open(filename_logreg, 'rb'))
result = loaded_model.score(X_test_pca, test["y_pred"])
print("pickle :" + result)

print(confusion_matrix(test["isFraud"],test["y_pred"]))
print(classification_report(test["isFraud"],test["y_pred"]))
print(accuracy_score(test["isFraud"],test["y_pred"]))
print(precision_score(test["isFraud"],test["y_pred"]))
print(recall_score(test["isFraud"],test["y_pred"]))
print(f1_score(test["isFraud"],test["y_pred"]))
