# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 07:46:51 2021

@author: Sabri
"""

#bbin_rec.py

def bbinaria_rec(lista, e):
    '''Precondición: lista es una lista ordenada de
    menor a mayor, e elemento a buscar
    Devuelve True si el elemento e está en la lista
    y False si no
    '''
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista) // 2
        if lista[medio] > e:
            lista = lista[:medio]
        elif lista[medio] < e:
            lista = lista[medio+1:]
        else:
            lista = [lista[medio]]
        res = bbinaria_rec(lista, e)
    return res

lista = [1, 2, 3, 4, 5]
bbinaria_rec(lista, -1)
