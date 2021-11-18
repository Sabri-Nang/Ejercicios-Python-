# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:58:20 2021

@author: Sabri
"""

import numpy as np
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
def ord_insercion(lista):
    '''Ordena una lista de elementos según el método de inserción.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista esta ordenada'''
    comparaciones  = 0
    for i in range(len(lista) - 1):
        if lista[i + 1] < lista[i]:
            comparacion = reubicar(lista, i + 1)
            
            comparaciones += comparacion
    return comparaciones
        
def reubicar(lista, p):
    '''Reubica al elemento que está en la posición p de la lista
    dentro del segmento [0: p-1].
    Pre: p tiene  que ser una posición válida de lista'''
    
    v = lista[p]
    
    #Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    #encontrar la posición  j tal que lista[j-1] <= v < lista[j]
    j = p
    comparaciones = 0
    while j > 0 and v < lista[j - 1]:
        lista[j] = lista[j - 1]
        j -= 1
        comparaciones += 1
    lista[j] = v
    return comparaciones

#%%
def ord_burbujeo(lista):
    '''Ordena una lista de elementos utilizando el método de burbujeo.
    Pre: Los elementos deben ser comparables.
    Post: La lista está ordenada. Devuelve la cantidad de comparaciones 
    realizadas.
    '''
    N = len(lista)
    j = 1
    comparaciones = 0
    while j < N:  #Recorro todos los elementos
        i = 1
        comparaciones += j #cantidad de comparaciones
        while i < len(lista):
            if lista[i-1] > lista[i]:
                lista[i - 1], lista[i] = lista[i], lista[i - 1]  #intercambio los elementos
            i += 1
        j += 1
    return comparaciones
  
#%%
def merge_sort(lista, comp = 0):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    #comp += 1  
    if len(lista) < 2:
        lista_nueva = lista
        comp += 1
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio], comp = comp)[0]
        der = merge_sort(lista[medio:], comp = comp)[0]
        lista_nueva, comparaciones = merge(izq, der, comp)
        comp += comparaciones + 1
    return lista_nueva, comp

def merge(lista1, lista2, comp):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    

    while(i < len(lista1) and j < len(lista2)):
        comp += 2
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, comp


    
#%%
    
def experimento_timeit(listas, num):
    '''
    Realiza un experimento usando timeit para evaluar los distintos métodos
    para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector para cada método. Devuelve cuatro arrays: tiempos_seleccion,
    tiempos_insercion, tiempos_burbujeo, tiempos_merge_sort.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica la cantidad de repeticiones
    a ejecutar el método para cada lista.
    '''
    tiempos_seleccion = []
    tiempos_insercion = []
    tiempos_burbujeo = []
    tiempos_merge = []
    
    global lista
    
    for lista in listas:
        
        #evalúo el método de selección
        #en una copia nueva ára cada iteración
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', 
                                     number = num,
                                     globals = globals())
                #guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())',
                                     number = num,
                                     globals = globals())
        #guardo el resultado
        tiempos_insercion.append(tiempo_insercion)
        
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())',
                                    number = num,
                                    globals = globals())
        tiempos_burbujeo.append(tiempo_burbujeo)
        
        tiempo_merge = tt.timeit('merge_sort(lista.copy())',
                                 number = num,
                                 globals = globals())
        tiempos_merge.append(tiempo_merge)
        

        
    #paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    tiempos_insercion = np.array(tiempos_insercion)
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    tiempos_merge = np.array(tiempos_merge)
    
    return tiempos_seleccion, tiempos_insercion, tiempos_burbujeo, tiempos_merge

#%%
np.random.seed(0)
listas = []
for N in range(1, 256):
    listas.append(generar_lista(N))
#%%   
tiempos_seleccion, tiempos_insercion, tiempos_burbujeo, tiempos_merge = experimento_timeit(listas, 2)

plt.figure()    
plt.plot(tiempos_seleccion, c='b', label='Selección')
plt.plot(tiempos_insercion, c = 'red', label='Inserción')
plt.plot(tiempos_burbujeo, c= 'orange', label='Burbujeo')
plt.plot(tiempos_merge, c = 'green', label = 'Merge Sort')
plt.xlabel('Longitud de la lista')
plt.ylabel('Tiempos')
plt.legend()
plt.show()



