# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 15:44:28 2021

@author: Sabri
"""
import numpy as np

def division(dividendo, divisor):
    '''Cálculo de la división
    
    Pre: Recibe dos números, divisor debe ser distinto de 0.
    Pos: Devuelve un número real, con el cociente de ambos.
    '''
    
    assert divisor != 0, 'El divisor no puede ser 0'
    return dividendo / divisor

def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
    Si hasta < desde, entonces devuelve cero.
    
    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
    [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    if desde < hasta:
        enteros = np.arange(desde, hasta+1)
        return enteros.sum()
    return 0
    
