# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 03:15:20 2021

@author: Sabri
"""
#Ejercicio 5.5


import random

  
def lista_temperaturas(N):   
    '''Dado un valor N devuelve una lista de N valores con las temperaturas obtenidas
    de medir una temperatura media de 37.5 °C con un termómetro con un
    error aleatorio normal con media 0 y desvío estándar de 0.2 grados 
    (error gaussiano)
    '''
    temperaturas=[37.5] * N
    for i, temperatura in enumerate(temperaturas):
        error = random.normalvariate(0, 0.2)
        temperaturas[i] = temperatura + error
        #print(f'{temperaturas[i]:.2f}', end=', ')
    temperaturas.sort()
    return temperaturas

temperaturas = lista_temperaturas(99)
maximo = max(temperaturas)
minimo = min(temperaturas)
promedio = sum(temperaturas)/len(temperaturas)

i_mediana=int((len(temperaturas) + 1) / 2) - 1
mediana = temperaturas[i_mediana]

print(f'\n\nEl máximo de temperaturas es: {maximo:.2f}')
print(f'El mínimo de temperaturas es: {minimo:.2f}')
print(f'El promedio de temperaturas es: {promedio:.2f}')
print(f'La mediana de temperaturas es: {mediana:.2f}\n')

#%% Ejercicio 5.9

import numpy as np
import os

temperatura = lista_temperaturas(999)
path_actual = os.getcwd()               #Guardo el path actual
os.chdir('../Data')                     #voy a la carpeta Data
np.save('Temperaturas', temperatura)    #Guardo la variable temperatura

os.chdir(path_actual)                   #Vuelvo a la carpeta de la cual partí


#%%
#Cuartiles
temperaturas=lista_temperaturas(99)
#i_q2 = int((len(temperaturas)-1)/2)  #indice para el cuartil 2 (mediana)
i_q1 = int((len(temperaturas) + 1) / 4 - 1)
i_q3 =int( 3 * (len(temperaturas) + 1) / 4 - 1)
q1 = temperaturas[i_q1]
q3 = temperaturas[i_q3]

print(f'\n\nPrimer cuartil: {q1:.2f}')
print(f'Tercer cuartil: {q3:.2f}')

