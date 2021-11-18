# -*- coding: utf-8 -*-
"""
Created on Mon May 24 03:14:36 2021

@author: Sabri
"""

#Generadores
#generador es una función que define un patrón de iteración

def regresiva(n):
    print('Cuenta regresiva desde', n)
    while n > 0:
        yield n
        n -= 1
#generador es cualquier función que usa el comando yield
#yield produce un valor y luego suspende la ejecución de la 
#función
#La ejecución continúa al volver a llamar __next__()

        
for x in regresiva(10):
    print(x, end = ' ')
    
#%%
def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line

for line in open('../Data/camion.csv'):
    print(line, end = '')
    
for line in filematch('../Data/camion.csv', 'Naranja'):
    print(line, end = '')