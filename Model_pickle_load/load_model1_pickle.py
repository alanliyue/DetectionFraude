
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


from sklearn.metrics import f1_score



import pickle
from sklearn.preprocessing import StandardScaler

# On importe le dataset


df = pd.read_csv("Projet_fraude.csv", sep=",")
# On supprime les colonnes pas utiles

df=df.drop(columns="nameDest")
df=df.drop(columns="nameOrig")
df=df.drop(columns="oldbalanceOrg")
df=df.drop(columns="newbalanceOrig")
df=df.drop(columns="oldbalanceDest")
df=df.drop(columns="newbalanceDest")

# On créé des dummies pour la colonne type

list_quali = ["type"]
df=pd.get_dummies(df,prefix="TOP", columns=list_quali)

# On sépare en train et test 80/20

train, test = train_test_split(df, test_size=0.2, stratify = df["isFraud"])
train, test = train.copy(), test.copy()

# On détermine les features 

features = [i for i in df.columns if i!= "isFraud"]
y = df['isFraud']
X = features

# On applique un SMOTE sur notre dataset

oversample = SMOTE(sampling_strategy=0.42)
x_train_smote, y_train_smote = oversample.fit_resample(train[X],train["isFraud"])

# On applique une standardisation des données



scaler = StandardScaler()
# Fit on training set only.
scaler.fit(x_train_smote)
# Apply transform to both the training set and the test set.
X_train_scaled = scaler.transform(x_train_smote)
X_test_scaled =scaler.transform(test[X])

# PCA

from sklearn.decomposition import PCA
# Make an instance of the Model
pca = PCA(.90)

pca.fit(X_train_scaled)

X_train_smote_pca = pca.transform(X_train_scaled)
X_test_pca =pca.transform(X_test_scaled)

# On load le model logreg
loaded_model = pickle.load(open('finalized_model_logreg.sav', 'rb'))
test["y_pred"] = loaded_model.predict(X_test_pca)
result = loaded_model.score(X_test_pca, test["y_pred"])


print(confusion_matrix(test["isFraud"],test["y_pred"]))
print(classification_report(test["isFraud"],test["y_pred"]))
print(accuracy_score(test["isFraud"],test["y_pred"]))
print(precision_score(test["isFraud"],test["y_pred"]))
print(recall_score(test["isFraud"],test["y_pred"]))
print(f1_score(test["isFraud"],test["y_pred"]))
