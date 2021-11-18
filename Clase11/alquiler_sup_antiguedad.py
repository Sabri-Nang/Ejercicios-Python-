# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 11:18:16 2021

@author: Sabri
"""

#superficie y antiguedad

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model



superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
antiguedad = np.array([50.0, 5.0, 25.0, 70.0])

data_deptos = pd.DataFrame({'alquiler': alquiler, 
                            'superficie': superficie, 
                            'antiguedad': antiguedad})

X = pd.concat([data_deptos.superficie, data_deptos.antiguedad], axis = 1)

ajuste_deptos = linear_model.LinearRegression()
ajuste_deptos.fit(X, data_deptos.alquiler)

errores = data_deptos.alquiler - (ajuste_deptos.predict(X))
print(errores)
print("ECM:", (errores**2).mean())  #error cuadrático medio

x = superficie + antiguedad
coef_superficie, coef_antiguedad = ajuste_deptos.coef_
c = ajuste_deptos.intercept_
print(f'Coeficiente de la superficie: {coef_superficie}')
print(f'coeficiente de la antiguedad: {coef_antiguedad}')

grilla_x_superficie = np.linspace(start = superficie.min() - 10, stop = superficie.max(), num = 1000)
grilla_x_antiguedad = np.linspace(start = antiguedad.min() - 10, stop = antiguedad.max(), num = 1000)
grilla_y = grilla_x_superficie * coef_superficie + grilla_x_antiguedad * coef_antiguedad + c


# data_deptos.plot.scatter('superficie', 'alquiler')
# plt.plot(grilla_x_superficie, grilla_y_superficie)
# plt.title('Alquiler vs Superficie')
# plt.show()

# grilla_x_antiguedad = np.linspace(start = antiguedad.min() - 10, stop = antiguedad.max(), num = 1000)
# grilla_y_antiguedad = grilla_x_antiguedad * b  + grilla_x_superficie*a + c


# data_deptos.plot.scatter('antiguedad', 'alquiler')
# plt.plot(grilla_x_antiguedad, grilla_y_antiguedad)
# plt.title('Alquiler vs Antiguedad')
# plt.show()

#A mayor superficie, ¿aumenta o disminuye el precio?
#El coeficiente de la superfice es 0.18, al aumentar la superficie aumenta el precio

#A mayor antigüedad, ¿aumenta o disminuye el precio?
#El coeficiente de la antiguedad es -0.01, al aumentar la antiguedad disminuye el precio

#¿Cuánto vale la ordenada al origen del modelo?
#La ordenada al origen vale 7.14

