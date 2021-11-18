# -*- coding: utf-8 -*-
"""
Created on Tue May 11 06:43:16 2021

@author: Sabri
"""

#ejercicio 8.7

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import numpy as np

direc1 = '..'
direc2 = 'Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(direc1, direc2, archivo)

df_lineal = pd.read_csv(fname)
cols_sel = ['nombre_cientifico', 'ancho_acera',
            'diametro_altura_pecho', 'altura_arbol']
df_lineal = df_lineal[cols_sel]

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 
                          'Tipuana tipu']

df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico']
                                .isin(especies_seleccionadas)]

#Ejercicio 8.8
#Realiza un boxplot de los diámetros de los árboles agrupados por especie
df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
plt.xlabel('Nombre Científico')

#boxplot alturas
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')
plt.xlabel('Nombre Científico')

#pairplot
sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
#en la diagonal tiene kdeplots (kernel density estimation plots una version
#suavizada delos histogramas. Y fuera de la diagonal scatterplots
#El hue selecciona la variable categórica a usar para distinguir subgrupos y 
#asociarles colores

#ancho acera no aparece en los gráficos porque tiene valores nan
