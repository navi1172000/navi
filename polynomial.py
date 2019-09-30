# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:12:29 2019

@author: naveen
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('Position_Salaries.csv')
X=data.iloc[:, 1:2].values
y=data.iloc[:, 2].values

"""from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=1/3,random_state=0)"""

from sklearn.linear_model import LinearRegression
l_reg=LinearRegression()
l_reg.fit(X,y)

from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=6)
X_poly=poly_reg.fit_transform(X)
l1_reg=LinearRegression()
l1_reg.fit(X_poly,y)

plt.scatter(X,y,color='red')
plt.plot(X,l_reg.predict(X),color='blue')
plt.title('truth vs linear regression')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()

plt.scatter(X,y,color='red')
plt.plot(X,l1_reg.predict(poly_reg.fit_transform(X)),color='blue')
plt.title('truth vs linear regression')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()