# -*- coding: utf-8 -*-
"""
Created on Mon May 31 03:41:28 2021

@author: Sabri
"""

#sumar_lista.py

def sumar(lista):
    '''Devuelve la suma de los elementos 
    en la lista'''
    res = 0
    if len(lista) != 0:
        res = lista[0] + sumar(lista[1::])
    return res

#%%
#Recursión de cola

def sumar(lista, suma = 0):
    '''Devuelve la suma del os elementos en la lista'''
    res = suma
    if len(lista) != 0:
        res = sumar(lista[1:], lista[0] + suma)
    return res

#%%
#suma por recursion

def sumar(lista):
    '''Devuelve la suma de los elementos de la lista'''
    suma = 0
    while lista:
        lista, suma = lista[1:], lista[0] + suma
    return suma