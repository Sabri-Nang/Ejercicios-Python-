# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:38:36 2021

@author: Sabri
"""

import numpy as np
import time
import timeit as tt
import matplotlib.pyplot as plt

def generar_lista(N):
    '''Genera una lista de largo N con números enteros del 1 al 1000
    '''
    ar = np.random.randint(1, 1001, N)
    lista = list(ar)

    return lista

#%%
def ord_seleccion(lista):
    '''Ordena una lista de elementos según el método de selección.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada'''
    
    # posición final del segmento a tratar
    n = len(lista) - 1
    
    comparaciones = 0
    #mientras haya al menos 2 elementos para ordenar
    while n > 0:
        #posición del mayor valor del segmento
        p, comparacion = buscar_max(lista, 0, n)
        
        #comparacion = n - 0
        comparaciones += comparacion
        
        # intercambiar el valor que está en p con el valor que
        #está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)
        
        #reducir el segmento en 1
        n = n - 1
    return comparaciones
        
def buscar_max(lista, a, b):
    '''Devuelve la posición del máximo elemento en un segmento de
    lista de elementos comparables.
    La lista no debe ser vacía.
    a y b son las posiciones inicial y final del segmento.'''
    
    pos_max = a
    comparacion = 0
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
        comparacion += 1
    return pos_max, comparacion

#%%

np.random.seed(0)
listas = []
for N in range(1, 256):
    listas.append(generar_lista(N))
    
def experimento_timeit_seleccion(listas, num):
    '''
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica la cantidad de repeticiones
    a ejecutar el método para cada lista.
    '''
    tiempos_seleccion = []
    
    global lista
    
    for lista in listas:
        
        #evalúo el método de selección
        #en una copia nueva ára cada iteración
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', 
                                     number = num,
                                     globals = globals())
        
        #guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        
    #paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    
    return tiempos_seleccion

#%%
tiempos_seleccion = experimento_timeit_seleccion(listas, 100)
plt.plot(tiempos_seleccion)