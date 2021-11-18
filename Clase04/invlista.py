# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 03:22:49 2021

@author: Sabri
"""

#invlista.py

def invertir_lista(lista):
    '''Dada una lista devuelve otra con los mismos elementos pero en orden
    inverso'''
    invertida=[]
    for e in lista:  #Recorro la lista
        invertida.insert(0,e)  #agrego el elemento e al principio de la lista invertida
    return invertida

#%%

invertir_lista([1, 2, 3, 4, 5])
invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
