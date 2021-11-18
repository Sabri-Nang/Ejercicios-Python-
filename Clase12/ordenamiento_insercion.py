# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 04:10:19 2021

@author: Sabri
"""

#ordenamiento_insercion

#consiste en fijarse desde el segundo elemento de la lista
#y compararlo con el/los anterior/es, se desplaza a derecha o izquierda
#según sea mayor o menor.

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
    
#lista = [3, 2, -1, 5, 0, 2]
#ord_insercion(lista)

#T(N) ~ c * (2 + 3 + *s + N) ~ c * N * (N+1)/2 ~ N^2
#Si la lista esta ordenada hace solo N pasos
#T(N) ~ N
