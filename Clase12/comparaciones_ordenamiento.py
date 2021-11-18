# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 12:22:58 2021

@author: Sabri
"""

import numpy as np
#from ordenamiento_seleccion import ord_seleccion
#from ordenamiento_insercion import ord_insercion
#from burbujeo import ord_burbujeo
#from comp_tres_metodos import generar_lista
import matplotlib.pyplot as plt


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
def ord_insercion(lista):
    '''Ordena una lista de elementos según el método de inserción.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista esta ordenada'''
    comparaciones  = 0
    for i in range(len(lista) - 1):
        if lista[i + 1] < lista[i]:
            comparacion = reubicar(lista, i + 1)
            
            comparaciones += comparacion
        #print("DEBUG: ", lista)
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
def generar_lista(N):
    '''Genera una lista de largo N con números enteros del 1 al 1000
    '''
    ar = np.random.randint(1, 1001, N)
    lista = list(ar)

    return lista
#%%

N = 256
np.random.seed(0)
comp_seleccion = [] #listas donde se guardan los promedios de las comparaciones
comp_insercion = []
comp_burbujeo = []
comp_merge_sort = []

for n in range (1, N):
    seleccion = []
    insercion = []
    burbujeo = []
    merge_sort_res = []
    for i in range(10):   #hago 10 listas por longitud
        lista1 = generar_lista(n)
        lista2 = lista1.copy()
        lista3 = lista1.copy()
        lista4 = lista1.copy()

        
    #Agrego las comparaciones para 10 listas de largo n a una lista por método
        seleccion.append(ord_seleccion(lista1))
        insercion.append(ord_insercion(lista2))
        burbujeo.append(ord_burbujeo(lista3))
        merge_sort_res.append(merge_sort(lista4)[1])
    
    #Para cada método calculo el promedio comparaciones de 10 listas de igual largo
    seleccion_promedio = sum(seleccion)/len(seleccion)
    insercion_promedio = sum(insercion) / len(insercion)
    burbujeo_promedio = sum(burbujeo) / len(burbujeo)   
    merge_sort_promedio = sum(merge_sort_res) / len(merge_sort_res)
    
    #Agrego los promedios a las listas
    comp_seleccion.append(seleccion_promedio)  
    comp_insercion.append(insercion_promedio)
    comp_burbujeo.append(burbujeo_promedio)
    comp_merge_sort.append(merge_sort_promedio)
    


plt.figure()    
plt.plot(comp_seleccion, c='b', label='Selección')
plt.plot(comp_insercion, c = 'red', label='Inserción')
plt.plot(comp_burbujeo, c= 'orange', linestyle='--', label='Burbujeo')
plt.plot(comp_merge_sort, c = 'green', label = 'Merge Sort')
plt.xlabel('Longitud de la lista')
plt.ylabel('Comparaciones')
plt.legend()
plt.show()
    