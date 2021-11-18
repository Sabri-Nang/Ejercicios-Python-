# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 07:50:09 2021

@author: Sabri
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([55.0, 38, 68, 70, 53, 46, 11, 16, 20, 4])
y = np.array([153.0, 98, 214, 220, 167, 145, 41, 63, 65, 25])
g = plt.scatter(x = x, y = y)
plt.title('scatterplot de los datos')
plt.show()

#Para ajustar y encontrar a y b que devuelvan la mejor
#recta, debemos minimizar la suma de los cuadrados de los 
#residuos
#Es decir debemos encontrar los valores de a y b tal que
# sum (a*x_i + b - y_i)^2  sea minimo
#derivamos respecto a a y b e igualamos a cero

def ajuste_lineal_simple(x, y):
    a = sum(((x - x.mean()) * (y - y.mean()))) / sum(((x - x.mean())**2))
    b = y.mean() - a * x.mean()
    return a, b
#%% Usando pandas y linear_model de sklearn
import pandas as pd
from sklearn import linear_model

x = np.array([55.0, 38, 68, 70, 53, 46, 11, 16, 20, 4])
y = np.array([153.0, 98, 214, 220, 167, 145, 41, 63, 65, 25])
datosxy = pd.DataFrame({'x': x, 'y': y})  #paso los datos a un dataframe

ajus = linear_model.LinearRegression()  # llamo al modelo de regresión lineal
ajus.fit(datosxy[['x']], datosxy['y'])  # ajusto el modelo

grilla_x = np.linspace(start = 0, stop = 70, num = 1000)
grilla_y = ajus.predict(grilla_x.reshape(-1, 1))

datosxy.plot.scatter('x', 'y')
plt.title('Ajuste lineal usando sklearn')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()

#%% Ejemplo: datos sintéticos

#Generamos 50 datos para la variable x
#Determinamos la variable y con una relación
#lineal más un error normal

import numpy as np

N = 50
minx = 0
maxx = 500
x = np.random.uniform(minx, maxx, N)
r = np.random.normal(0, 25, N)  #residuos simulados
y = 1.3 * x + r

g = plt.scatter(x = x, y = y)
plt.title('Gráfico de dispersión de los datos')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#ajustamos con lo visto antes
a, b = ajuste_lineal_simple(x, y)

grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
grilla_y = grilla_x * a + b

g = plt.scatter(x = x, y = y)
plt.title('y ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.xlabel('x')
plt.ylabel('y')

plt.show()


