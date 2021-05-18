print("df1")
from math import *

import csv
print("df2")
fichier = open("Projet_fraude.csv", "rt")
#f= open(r"/Applications/MAMP/htdocs/FRAUDE/Projet_fraude.csv")

print("df3")
lecteurCSV = csv.reader(fichier,delimiter=",")
print("df4")

#import csv;
#f= open (r"C:\Users\HP\Desktop/data.csv")
#myReader = csv.reader(f)
#for row in myReader:
#print(row)

import numpy as np
print("df4")
import matplotlib.pyplot as plt
print("df4")
import seaborn as sns
print("df4")


from sklearn.ensemble import RandomForestClassifier
print("df4")
from sklearn.linear_model import LogisticRegression
print("df4")
from sklearn.model_selection import train_test_split
print("df4")
from sklearn.model_selection import KFold, cross_val_score
print("df4")
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score, precision_score, plot_confusion_matrix
print("df4")

from scipy.special import boxcox1p
print("df4")
from scipy.stats import boxcox_normmax
print("df4")
from scipy.stats import skew, boxcox
print("df4")
from sklearn import preprocessing
print("df4")

