# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:20:48 2021

@author: Sabri
"""
import numpy as np
import matplotlib.pyplot as plt

#ejemplo relación cuadrática
def ajuste_lineal_simple(x, y):
    a = sum(((x - x.mean()) * (y - y.mean()))) / sum(((x - x.mean())**2))
    b = y.mean() - a * x.mean()
    return a, b


np.random.seed(3141)
N = 50
indep_vars = np.random.uniform(size = N, low = 0, high = 10)
r = np.random.normal(size = N, loc = 0.0, scale = 8.0) #residuos
dep_vars = 2 + 3 * indep_vars + 2 * indep_vars**2 + r #relación cuadrática

plt.figure()
x = indep_vars
y = dep_vars
plt.scatter(x, y)
plt.title('Scatterplot de los datos')
plt.show()

a, b = ajuste_lineal_simple(x, y)

grilla_x = np.linspace(start = 0, stop = 10, num = 1000)
grilla_y = grilla_x * a + b
plt.figure()
g = plt.scatter(x = x, y = y)
plt.title('Ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()


#errores y error cuadrático medio (ECM)
errores = y - (x * a + b)
print("ECM", (errores**2).mean())

xc = x**2
ap, bp = ajuste_lineal_simple(xc, y)
grilla_y_p = (grilla_x**2) * ap + bp
plt.figure()
plt.scatter(x, y) 
plt.plot(grilla_x, grilla_y, c = 'green')
plt.plot(grilla_x, grilla_y_p, c = 'red')
plt.title('Ajuste lineal con x^2')
plt.show()

#Errores

yhat = (x**2) * ap + bp    # valores estimados
residuos = y - yhat        # diferencia entre el valor original y el estimado
ecm = (residuos**2).mean() # error cuadrático medio
print("ECM:", ecm)

#%%
from sklearn import linear_model

x = indep_vars
cx = x**2
y = dep_vars

X = np.concatenate((x.reshape(-1,1),xc.reshape(-1,1)),axis=1)

lm = linear_model.LinearRegression()
lm.fit(X, y)
a, b = lm.coef_
c = lm.intercept_

plt.figure()
grilla_x = np.linspace(start = 0, stop = x.max(), num = 1000)
grilla_y = a*grilla_x + b*grilla_x**2+c
plt.scatter(x, y)
plt.plot(grilla_x, grilla_y, c = 'green', label = 'Usando x y x^2')

#Errores

yhat = (x**2) * b + a * x + c    # valores estimados
residuos = y - yhat        # diferencia entre el valor original y el estimado
ecm = (residuos**2).mean() # error cuadrático medio
print("ECM:", ecm)


lm = linear_model.LinearRegression()
lm.fit(xc.reshape(-1, 1), y)
a = lm.coef_
c = lm.intercept_
grilla_y = a * grilla_x **2 + c
plt.plot(grilla_x, grilla_y, c = 'red', label = 'Usando xc')
#Errores

yhat = (xc**2) * a + c    # valores estimados
residuos = y - yhat        # diferencia entre el valor original y el estimado
ecm = (residuos**2).mean() # error cuadrático medio
print("ECM:", ecm)

plt.legend()
plt.show()



