# -*- coding: utf-8 -*-
"""
Created on Mon May 31 04:52:47 2021

@author: Sabri
"""

def es_potencia(n, b):
    '''Recibe dos enteros n y b.
    Devuelve True si n es potencia de b y False
    si no lo es
    '''
    #caso base 
    if n == 1:
        return True
    else:
        if n % b == 0:  
            n = n / b
            return es_potencia(n, b)
        else:    #si no son múltiplos no será potencia
            return False

    