# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 02:09:47 2021

@author: Sabri
"""

def busqueda_con_index(lista, e):
    '''Busca un elemento e en la lista.

    Si e está en lista devuelve el índice,
    de lo contrario devuelve -1.
    '''
    if e in lista:
        pos = lista.index(e)
    else:
        pos = -1
    return pos