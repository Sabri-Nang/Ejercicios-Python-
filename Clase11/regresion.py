# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 01:59:49 2021

@author: Sabri
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
import numpy as np

#%%
x  = np.random.uniform(0, 10, 25)
y = 2 * x - 8
plt.scatter(x, y)
plt.hist(x, bins=15)

#%%
N = 25 #cantidad de datos
x = np.random.uniform(0, 10, N)
r = np.random.normal(0, 1, N)   #residuo error
#distribicuon normal con media 0 y desvio 1
y = 2 * x - 8 + r
#plt.plot(x, 2 * x - 8, c = 'g')
#plt.scatter(x, y)

#%
modelo = linear_model.LinearRegression() #llamo al modelo regresion
modelo.fit(x.reshape(-1, 1), y)  #ajusto el modelo

#%
a = modelo.coef_[0]
b = modelo.intercept_
print(a, b)

L = np.array([0,10])
plt.scatter(x, y)
plt.plot(L, 2 * L - 8, c = 'g', label = 'realidad')
plt.plot(L, a * L + b, c = 'r', linestyle = '-.', label = 'modelo')
plt.legend()

#%%
L = np.array([0, 10])
ysombrero = a*x + b
plt.scatter(x, y, c = 'g', label = r'$\hat{y}$')
plt.plot(L, a*L+b, c='b', label = 'y')

plt.plot(L, a*L+b, c='r', linestyle='-.', label='modelo')
for i, d in enumerate(x):
    if i == 0:
        plt.plot([d, d], [y[i], ysombrero[i]], c='b', label='residuos')
    else:
        plt.plot([d, d], [y[i], ysombrero[i]], c='b')
plt.legend()