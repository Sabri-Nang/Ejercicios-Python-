# -*- coding: utf-8 -*-
"""
Created on Mon May 31 02:36:19 2021

@author: Sabri
"""

#potencia.py

#potencia por recursion
def _potencia(b, n, str_tab = ''):
    '''Precondición n:>0
    Devuelve: b^n '''
    
    if n == 0:
        print(f'{str_tab} Llegue')
        return 1
    if n < 0:
        b = 1 / b
        n = -n
        return _potencia(b, n)
    if n % 2 == 0: 
        #caso par
        p = _potencia(b, n // 2, str_tab + '\t')
        print(f'{str_tab} potencia({b}, {n//2})')
        return p * p
    else:
        #caso impar
        p = _potencia(b, (n - 1) // 2, str_tab + '\t')
        print(f'{str_tab} Hice potencia({b}, {(n-1)//2})')
        return p * p * b
    
#%%
#potencia iterativo

def potencia(b, n):
    '''Precondición: n >= 0
    Devuelve: b^n
    '''
    
    pila = []
    while n > 0:
        if n % 2 == 0:
            pila.append(True)
            n //= 2
        else:
            pila.append(False)
            n = (n - 1) // 2
    p = 1
    while pila:
        es_par = pila.pop()
        if es_par:
            p *= p
        else:
            p *= p * b
    return p