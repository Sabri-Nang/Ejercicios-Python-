# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 12:05:05 2021

@author: Sabri
"""

import requests
import io
import pandas as pd
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt



enlace = 'https://raw.githubusercontent.com/python-unsam/Programacion_en_Python_UNSAM/master/Notas/11_Recursion/longitudes_y_pesos.csv'
r = requests.get(enlace).content
data_lyp = pd.read_csv(io.StringIO(r.decode('utf-8')))

x = data_lyp['longitud']
y = data_lyp['peso']
ajus = linear_model.LinearRegression(fit_intercept = False)
ajus.fit(data_lyp[['longitud']], data_lyp['peso'])

grilla_x = np.linspace(start = 0, stop = data_lyp['longitud'].max(), num = 1000)
grilla_y = ajus.predict(grilla_x.reshape(-1, 1))

data_lyp.plot.scatter('longitud', 'peso')
plt.title('Ajuste lineal usando sklearn')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()

a = ajus.coef_
b = ajus.intercept_

print(f'El peso específico es {a[0]}')



