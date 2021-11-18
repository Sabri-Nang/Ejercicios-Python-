# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 04:18:28 2021

@author: Sabri
"""

#propaga.py

def propagar(lista):
    '''Recibe un vector con 0's, 1's y -1's y devuelve un vector en el que los 
    1's se propagaron a sus vecinos con 0'''
    l=len(lista)-1
    
    
    for i in range(l):
        
        if lista[i]==1 and lista[i+1]==0:
            lista[i+1]=1
    for i in range(l,0,-1):
        
        if lista[i]==1 and lista[i-1]==0:
            lista[i-1]=1
    return lista
            
            
        
propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
propagar([ 0, 0, 0, 1, 0, 0])