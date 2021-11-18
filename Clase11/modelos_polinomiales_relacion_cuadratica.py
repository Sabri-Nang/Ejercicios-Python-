# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:15:01 2021

@author: Sabri
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

def AIC(k, ecm, num_params):
    '''Calcula el AIC de una regresión lineal múltiple de 'num_params' 
    parámetros, ajustada sobre una muestra de 'k' elementos, y que da lugar 
    a un error cuadrático medio 'ecm'.'''
    aic = k * np.log(ecm) + 2 * num_params
    return aic


np.random.seed(3141)
N = 50
indep_vars = np.random.uniform(size = N, low = 0, high = 10)
r = np.random.normal(size = N, loc = 0.0, scale = 8.0) #residuos
dep_vars = 2 + 3 * indep_vars + 2 * indep_vars**2 + r #relación cuadrática

x = indep_vars
xc = x**2
y = dep_vars

def pot(x,n):
    X=x.reshape(-1,1)
    for i in range(n-1):
        X=np.concatenate((X,(x**(i+2)).reshape(-1,1)),axis=1)
    return X

#X = np.concatenate((x.reshape(-1,1),xc.reshape(-1,1)),axis=1)
for i in range(1, 20, 1):
    X = pot(x, i)
    lm = linear_model.LinearRegression()
    lm.fit(X, y)

    
    #print(X.shape)
    #print(lm.coef_)
    coef=lm.coef_.reshape(1,-1)
    #print(coef)
    #print(lm.coef_.shape)
    yhat = (X*lm.coef_).sum(axis=1)+lm.intercept_
       # valores estimados
    residuos = y - yhat        # diferencia entre el valor original y el estimado
    ecm = (residuos**2).mean() # error cuadrático medio
    aic = AIC(len(y), ecm, i+1)
    print('-'*10)    
    print(f'Grado del polinomio {i}')
    print(f'Cantidad de parametros: {i+1}')
    print(f'ECM: {round(ecm, 2)}')
    print(f'AIC: {round(aic, 2)}')
    print('-'*10)
    
   
    
