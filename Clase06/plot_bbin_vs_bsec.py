# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 16:54:26 2021

@author: Sabri
"""

import random

#Obs: en lugar de poner las funciones busqueda_secuencial_ y busqueda binaria
#podría importarlas de busqueda_en_lista. Lo dejo de esta forma por la corrección
#de pares. 

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria.
    Precondición: la lista está ordenada.
    Devuelve una tupla cuyo primer elemento es -1 si x no está en la lista
    o p tal que lista[p] == x si x está en la lista. Y su segundo elemento
    es la cantidad de comparaciones que realizó.
    '''
    if verbose:
        print('[DEBUG] izq | der | medio')
    pos = -1 #Inicializo respues, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comps = 0
    while izq<=der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} | {der:>3d} | {medio:3d}')
        if lista[medio] == x:
            pos = medio   #elemento encontrado!
        if lista[medio] > x:
            der = medio-1 #descarto la mitad derecha
        else:             #if lista[medio] < x :
            izq = medio + 1 #descarto mitad izquierda
        comps += 1
    return pos, comps

def generar_lista(n, m):
    '''Recibe un int n y un int m.
    Devuelve una lista de n elementos entre 0 y m-1
    '''
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    '''Recibe un int m y devuelve un int aleatorio entre 0 y m-1
    '''
    return random.randint(0, m-1)

def experimento_secuencial_promedio(lista, m, k):
    '''Recibe una lista, un elemento m a buscar en la lista y un valor k
    cantidad de experimentos elementales que realizara.
    Busca el elemento realizando una búsqueda secuencial
    '''
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista, x)[1]
    
    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    '''Recibe una lista, un elemento m a buscar en la lista y un valor k, cantidad
    de experimentos elementales que realizará. 
    Busca el elemento realizando una búsqueda binaria.
    '''
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista, x)[1]
    comps_prom = comps_tot / k
    return comps_prom
    

#%%

import matplotlib.pyplot as plt
import numpy as np

m = 10000
k = 1000

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio_secuencial = np.zeros(256) # aca guardo el promedio de comparaciones secuencial sobre una lista de largo i, para i entre 1 y 256.
comps_promedio_binaria = np.zeros(256)    #guardo el promedio de comparaciones binarias sobre una lista de largo i, para i entre 256.
for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio_secuencial[i] = experimento_secuencial_promedio(lista, m, k)
    comps_promedio_binaria[i] = experimento_binario_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.figure()
plt.plot(largos,comps_promedio_secuencial, label = 'Búsqueda Secuencial')
plt.plot(largos, comps_promedio_binaria, label = 'Búsqueda Binaria')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()




