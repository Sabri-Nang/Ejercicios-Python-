# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 10:47:28 2021

@author: Sabri
"""

import numpy as np
from ordenamiento_seleccion import ord_seleccion
from ordenamiento_insercion import ord_insercion
from burbujeo import ord_burbujeo

def generar_lista(N):
    '''Genera una lista de largo N con números enteros del 1 al 1000
    '''
    ar = np.random.randint(1, 1001, N)
    lista = list(ar)

    return lista

#experimento 
np.random.seed(0)
N = 10
k = 100
listas = []
comp_seleccion = np.array([])
comp_insercion = np.array([])
comp_burbujeo = np.array([])
for n in range(k):
    lista1 = generar_lista(N)
    comp_seleccion = np.append(comp_seleccion, ord_seleccion(lista1))

    #comp_seleccion.append(ord_seleccion(lista1))
    
np.random.seed(0)
for n in range(k):
    lista2 = generar_lista(N)
    comp_insercion = np.append(comp_insercion, ord_insercion(lista2))
    #comp_insercion.append(ord_insercion(lista2))
    
np.random.seed(0)
for n in range(k):
    lista3 = generar_lista(N)
    comp_burbujeo = np.append(comp_burbujeo, ord_burbujeo(lista3))
    #comp_burbujeo.append(ord_burbujeo(lista3))

print(f'Listas de largo {N}')
print('Promedio cantidad de comparaciones')
print(f'Método SELECCIÓN: {comp_seleccion.mean()}')
print(f'Método INSERCIÓN: {comp_insercion.mean()}')
print(f'Método BURBUJEO: {comp_burbujeo.mean()}')