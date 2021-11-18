# -*- coding: utf-8 -*-
"""
Created on Mon May 10 03:27:06 2021

@author: Sabri
"""

import pandas as pd
import os

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio, archivo)
df = pd.read_csv(fname)

df[['altura_tot', 'diametro', 'inclinacio']].describe()

#seleccion
#fila de nombre_com

df['nombre_com'].unique() #ver todos los nombres
df['nombre_com'] == 'Ombú'  #seleccionar solo datos de Ombú

#cuantos Ombúes hay
(df['nombre_com'] == 'Ombú').sum()

#Contar todos los ejemplares
cant_ejemplares = df['nombre_com'].value_counts()

#Filtros booleanos
#se usan para filtrar esas filas en el dataframe
df_jacarandas = df[df['nombre_com'] == 'Jacarandá']  #esto genera una vista
                                                     #no copia la información
                                                     
cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]
df_jacarandas.tail()

#uso describe() para ver datos relevantes
df_jacarandas.describe()

#si quiero modificar df_jacarandas tengo que generar una copia
df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()

#%%Scatterplots

df_jacarandas.plot.scatter(x = 'diametro', y = 'altura_tot')


#Seaborn
import seaborn as sns

sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot')

#%% Filtros por índice y posición

cant_ejemplares = df['nombre_com'].value_counts()  #es una Serie, un DataFrame de una columna
cant_ejemplares.index

#para acceder a una fila a través de su índice:
df.loc[165]

#para acceder por número de posición
df_jacarandas.iloc[0]
###Son el mismo elemento, solo que la posicion 0, tiene el indice 165

#puedo accedes usando slice
cant_ejemplares.iloc[0:3]

#se pueden seleccionar filas y columnas, si separamos con comas las respectivas selecciones
df_jacarandas.iloc[-5:,2]
#toma las últimas 5 filas, y la tercer columna
#iloc[filas, columnas]
list(cant_ejemplares[1:4].index)
especies_seleccionadas = list(cant_ejemplares[1:4].index)
df_seleccion = df[df['nombre_com'].isin(especies_seleccionadas)]

sns.scatterplot(data = df_seleccion, x = 'diametro', y = 'altura_tot', hue = 'nombre_com', alpha = 0.3)
#%% Selección de columnas
#Al seleccionar una columna se obtiene una serie

df_jacarandas_diam = df_jacarandas['diametro']
type(df_jacarandas)
type(df_jacarandas_diam)

#%% Series temporales

#Pandas tiene gran potencial para el manejo de series temporales

pd.date_range('20200923', periods = 7)

pd.date_range('20200923 14:00', periods = 7)

pd.date_range('20200923 14:00', periods = 6, freq = 'H')

#Luego se pueden usar esos índices junto con datos para armar series
#temporales o DataFrames

pd.Series([1, 2, 3, 4, 5, 6], index = pd.date_range('20200923 14:00', periods = 6, freq = 'H'))

#%% Caminatas al azar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1, 2, 120), index = idx)
s2 = s1.cumsum()

plt.figure()
s2.plot()

#usar una media móvil (rolling mean) para suavizar los datos
w = 5 #ancho en minutos de la ventana
s3 = s2.rolling(w, min_periods = 1).mean() #min_periods especifica el numero minimo de observaciones en una ventana
                                           #tiene q ser menor o igual que el tamaño de la ventana 
plt.figure()
s3.plot()

#plt.show()

df_series_23 = pd.DataFrame([s2, s3]).T  #armo un dataframe con ambas series
df_series_23.plot()

#plt.figure()

#%% 12 Personas caminando 8 horas

#En este ejemplo creamos un índice que contenga un elemento por minuto a partir
#del comienzo de la clase y durante 8 horas
#Armamos también una lista de nombres

horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés', 'Bartolomé', 'Tiago', 
           'Isca', 'Tadeo', 'Mateo', 'Felipe', 'Simón', 'Tomás']

#usamos el modulo random de numpy para generar pasos para cada persona para 
#cada minuto. Los acumulamos con cumsum y los acomodamos en un DataFrame, usando
#el índice generado antes y poniéndoles nombres adecuados a cada columna

df_walks = pd.DataFrame(np.random.randint(-1, 2, [horas*60, 12])
                       .cumsum(axis=0), 
                       index = idx, columns = nombres)
#np.random.randint(a, b, [X, Y]) genera una matriz de X filas y Y columnas
#con elementos random entre [-1,2)
#luego .cumsum(axis=0) hace la suma acumulada en el axis = 0 (filas)
df_walks.plot()

#ahora lo suavizo usando min_periods para no perder datos de los extremos
w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean()  #datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav #cambio el nombre de las columnas
                             #para los datos suavizados
df_walk_suav.plot()
plt.legend(loc='best', ncol = 3) #, shadow=True, fontsize='x-large')

#Guardar serie o dataframe
df_walk_suav.to_csv('caminata_apostolica.csv')



