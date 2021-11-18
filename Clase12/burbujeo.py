# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 10:05:58 2021

@author: Sabri
"""

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
  
#%% Ordenamiento burbujeo recursivo
def ord_burbujeo_rec(lista):
    '''Ordena una lista de elementos utilizando el método de burbujeo.
    Pre: Los elementos deben ser comparables.
    Post: La lista está ordenada.
    Devuelve la lista y la cantidad de comparaciones que realizó
    '''
    comparaciones = 0
    if len(lista) <= 1:
        return lista, comparaciones
    else:
        for i in range(len(lista) - 1):
            comparaciones += i + 1  #Sumo las comparaciones para cada i
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                n = len(lista) - 1
                lista[:n], comp= ord_burbujeo_rec(lista[:n])
                

        return lista, comparaciones
      
#%%
#T(N) = c * (1+2+3+...+N) = c*N*(N-1)/2

lista_1 = [1, 2, -3, 8, 1, 5]
ord_burbujeo(lista_1)
lista_2 = [1, 2, 3, 4, 5]
lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
lista_4 = [10, 8, 6, 2, -2, -5]
lista_5 = [2, 5, 1, 0]
