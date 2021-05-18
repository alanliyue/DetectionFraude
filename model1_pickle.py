# On importe le dataset

import pandas as pd
df = pd.read_csv("Projet_fraude.csv", sep=",")

# On importe toutes les librairies dont on aura besoin

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

from scipy.special import boxcox1p
from scipy.stats import boxcox_normmax
from scipy.stats import skew, boxcox
from sklearn import preprocessing

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

oversample = SMOTE(ratio=0.42)
x_train_smote, y_train_smote = oversample.fit_resample(train[X],train["isFraud"])

# On applique une standardisation des données

from sklearn.preprocessing import StandardScaler

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

# On définit le modele KNeighborsClassifier en neigh avec des paramètres trouvés précédemment

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(metric= 'euclidean', n_neighbors= 2, weights= 'distance')

# On entraîne le modele sur les données d'entrainements

neigh.fit(X_train_smote_pca, y_train_smote)
test["y_pred"] = neigh.predict(X_test_pca)

# On utilise pickle
import pickle
filename_knn = 'finalized_model_knn.sav'
pickle.dump(neigh, open(filename_knn, 'wb'))















