# -*- coding: utf-8 -*-
"""
Created on Mon May 31 04:23:40 2021

@author: Sabri
"""

#numeros_triangulares.py
        
def n_triangular(n):
    '''
    Precondición: n>0
    Devuelve la suma de 1 a n, o dicho de otra forma
    el número triángular de n
    '''
    #caso base n==1
    if n == 1:
        return 1
    else:
        return n + n_triangular(n - 1)