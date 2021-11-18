# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 03:34:08 2021

@author: Sabri
"""

#replicar.py

#Escribir una función recursiva para replicar los elementos
#de una lista una cantidad n de veces
#Ejemplo replicar([1, 3, 3, 7], 2) -> [1, 1, 3, 3, 3, 3, 7, 7]


def replicar(lista, n):
    '''Recibe una lista y un número natural.
    Devuelve una lista con cada elemento replicado 
    la cantidad n de veces.
    '''
    if len(lista) == 1:
        return lista * n
    else:
        replicado = [replicar([elem], n) for elem in lista]
        return [elem for lis in replicado for elem in lis]
    