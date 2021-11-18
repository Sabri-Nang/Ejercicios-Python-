# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 03:40:37 2021

@author: Sabri
"""

#propaga.py

def propagar(lista):
    '''Recibe un vector con 0's, 1's y -1's y devuelve un vector en el que los 
    1's se propagaron a sus vecinos con 0'''
    l=len(lista)-1
    i=0
    while i<l:              #recorre desde i=0 hasta el penúltimo lugar (len(lista)-2)
                            #se corta cuando i=l=len(lista)-1
                            #Recorro de izquierda a derecha
        
        if lista[i]==1 and lista[i+1]==0:
            lista[i+1]=1    #si la en la posición siguiente a un elemento 1 hay
                            #un 0 lo reemplazo por un 1
        i+=1                #salgo con i=l  
   
    while i>0:              #Recorro desde i=l a i=1
                            #recorro de derecha a izquierda
        if lista[i]==1 and lista[i-1]==0:
            lista[i-1]=1    #si en la posición anterior a un elemento 1 hay un 0
                            #lo reemplazo por un 1
        i-=1                #salgo con i=0
    return lista
            
            
        
propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
propagar([ 0, 0, 0, 1, 0, 0])
propagar([0,0,-1,0,1])
propagar([])
