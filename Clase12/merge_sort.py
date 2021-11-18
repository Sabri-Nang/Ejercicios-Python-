# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:17:06 2021

@author: Sabri
"""
import random

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

#lista = [10, 8, 6, 2, -2, -5]
#merge_sort(lista)
    
#lista = [5, 4, 8, 1, 3, 7]
#merge_sort(lista)        



                