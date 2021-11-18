# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 03:33:23 2021

@author: Sabri
"""

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
    #comps = b - a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
        comparacion += 1
    return pos_max, comparacion

#En cada paso, buscar_lista hace tantos pasos como elementos en el
#segmento -> T(N) = c * (2 + 3 + 4 +...+ N) ~ c * (N + 1) * N/2 ~ N^2

lista = [3, 2, -1, 5, 0, 2]
ord_seleccion(lista)