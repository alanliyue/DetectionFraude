import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE



from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score, precision_score, plot_confusion_matrix

from scipy.special import boxcox1p
from scipy.stats import boxcox_normmax
from scipy.stats import skew, boxcox
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,precision_score, recall_score


# On load le model logreg
loaded_model = pickle.load(open(filename_knn, 'rb'))
result = loaded_model.score(X_test_pca, test["y_pred"])
print("pickle :" + result)

print(accuracy_score(test["isFraud"],test["y_pred"]))
print(precision_score(test["isFraud"],test["y_pred"]))
print(recall_score(test["isFraud"],test["y_pred"]))
print(f1_score(test["isFraud"],test["y_pred"]))
print(confusion_matrix(test["isFraud"],test["y_pred"]))


from sklearn.metrics import roc_curve
y_pred_prob=neigh.predict_proba(X_test_pca)[:,1]
fpr, tpr, thresholds = roc_curve(test["y_pred"], y_pred_prob)

plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr, label='KNeighborsClassifer')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('KNeighborsClassifer ROC Curve')
plt.show()


from sklearn.metrics import roc_auc_score

y_pred = neigh.predict_proba(X_test_pca)[:,1]
roc_auc_score(test["isFraud"], y_pred)
