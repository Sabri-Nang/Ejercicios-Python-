# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 02:18:38 2021

@author: Sabri
"""

def busqueda_lineal(lista,e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1'''
    pos=-1          #comenzamos suponiendo que e no está
    i=0
    for z in lista: #recorremos los elementos dela lista
        if z==e:    #si encontramos a e
            pos=i
            break
        i+=1
    return pos

#%%busqueda lineal con enumerate

def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

busqueda_lineal([1, 4, 54, 3, 0, -1], 44)
busqueda_lineal([1, 4, 54, 3, 0, -1], 3)
busqueda_lineal([1, 4, 54, 3, 0, -1], 0)
busqueda_lineal([], 42)


#El algoritmo de búsqueda lineal tiene un comportamiento proporcional a la 
#longitud de la lista involucrada, o que es un algoritmo lineal.