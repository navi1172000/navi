# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 19:56:15 2019

@author: naveen
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('IRIS.csv')
X=dataset.iloc[:, :-1].values
y=dataset.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder=LabelEncoder()
y=labelencoder.fit_transform(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=0)

from sklearn.svm import SVC
classifier= SVC(kernel='rbf',random_state=0)
classifier.fit(X_train,y_train)


y_p=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_true=y_test,y_pred=y_p)

from sklearn.metrics  import accuracy_score
acc=accuracy_score(y_true=y_test,y_pred=y_p)




