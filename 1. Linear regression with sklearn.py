# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:59:35 2019

@author: Administrator
"""

# The data science course 2019
# section 34: advanced statistical models - linear regression with sklearn
# Scikit-learn(sklearn) is built on Numpy, SciPy, and matplotlib
# We need to transform the data from panda data frames to NumPy ndarray before feeding to sklearn
# Including most machine learning methods except deep learning
#

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  #data visualization
sns.set()

from sklearn.linear_model import LinearRegression

# task: predicting GPA(dependent var) using SAT score(independent var)
# Prediction of GPA(target) using a single feature (supervised learning)

os.chdir("C:\\Users\\Administrator\\Desktop\\Python")
data = pd.read_csv("1.01. Simple linear regression.csv")

#use data.head() to check the first few lines

x = data['SAT']
y = data['GPA']

# use data.shape to check dimensions


#Regression 
reg = LinearRegression()
#reshape to 2-dimensional (b/c sklearn expect multiple features)
x_matrix = x.values.reshape(-1,1)

reg.fit(x_matrix, y) #(input, target)


#Output: LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
#normalization: subtract the mean but divide by the L2-norm of the inputs
#copy_X: copy the x value before fitting them (against transformations)
#fit_intercept=TRUE
#n_jobs: is parameter used when we want to parallelize routines (CPU used)

#R-squared
reg.score(x_matrix, y) 
#Coefficents, intercept
reg.coef_
reg.intercept_

#making prediction
reg.predict(1740) #predict with one input value


new_data = pd.DataFrame(data=[1740, 1760], columns=['SAT'])
reg.predict(new_data)
new_data['Predicted_GPA'] = reg.predict(new_data)

#plot it
plt.scatter(x,y)
yhat = reg.coef_*x_matrix + reg.intercept_

fig = plt.plot(x, yhat, lw=4, c='orange', label='regression line')
plt.xlabel('SAT', fontsize=20)
plt.ylabel('GPA', fontsize=20)
plt.show()


#Multiple linear regression