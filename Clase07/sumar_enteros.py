# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 15:58:02 2021

@author: Sabri
"""

#Ejercicio 7.6

#Implementación 1. Usando un ciclo

def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
    Si hasta < desde, entonces devuelve cero.
    
    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
    [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0
    if desde < hasta:
        for i in range(desde, hasta+1):
            suma += i
    return suma
        


#%% Implementación 2: sin ciclo


def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
    Si hasta < desde, entonces devuelve cero.
    
    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
    [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0
    if desde < hasta:
        suma = (hasta * (hasta + 1) - (desde - 1) * desde) / 2
    return suma