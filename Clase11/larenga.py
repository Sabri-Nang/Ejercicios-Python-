# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 04:18:19 2021

@author: Sabri
"""

def pascal(n, k):
    '''Recibe dos números enteros mayores o iguales a cero.
    n es la fila del triángulo empezando desde n = 0 de arriba a abajo
    k es el elemento de la fila, empezando desde k = 0 de izquierda a derecha
    k <= n
    Devuelve el valor que se encuentra en la fila n y la columna
    k del triángulo de pascal'''
    if k == 0 or n == k:  #si k=0 o k=n es la posición de un borde
        return 1
    elif k > n:
        print('k debe ser menor o igual que n')
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)