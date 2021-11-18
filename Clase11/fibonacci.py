# -*- coding: utf-8 -*-
"""
Created on Mon May 31 03:22:16 2021

@author: Sabri
"""

#fibonacci.py

def fib(n):
    '''Precondición: n >= 0
    Devuelve: el número de Fibonacci número n
    '''
    if n == 0 or n == 1:
        return n
    ant2 = 0
    ant1 = 1
    for i in range(2, n + 1):
        fibn = ant1 + ant2
        ant2 = ant1
        ant1 = fibn
    return fibn