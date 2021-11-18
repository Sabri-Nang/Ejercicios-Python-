# -*- coding: utf-8 -*-
"""
Created on Mon May 31 04:31:23 2021

@author: Sabri
"""

#digitos.py

def digitos(n):
    '''Recibe un número positivo entero mayor que 1.
    Devuelve la cantidad de dígitos'''
    # if n < 1:
    #     n = 1 / n
    #     return digitos(n)
    if n / 10 < 1:
        return 1
    else:
        return 1 + digitos(n / 10)