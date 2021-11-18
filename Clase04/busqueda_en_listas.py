# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 02:29:42 2021

@author: Sabri
"""

def buscar_u_elemento(lista, e):
    '''Recibe una lista y un elemento y devuelve la posición de la última 
    aparición de ese elemento en la lista o -1 si no pertenece a la lista'''
    pos=-1
    i= len(lista)-1
    while i>=0:
        
        if lista[i]==e:
            pos=i
            break
        i-=1
    return pos
    

buscar_u_elemento([1,2,3,2,3,4],1)
buscar_u_elemento([1,2,3,2,3,4],2)
buscar_u_elemento([1,2,3,2,3,4],3)
buscar_u_elemento([1,2,3,2,3,4],5)

#%%buscar_n_elemento

def buscar_n_elemento(lista, e):
    '''Recibe una lista y un elemento y devuelve la cantidad de veces que 
    aparece el elemento en la lista'''
    i=0
    for l in lista:
        if l==e:
            i+=1
    return i

buscar_n_elemento([1,2,3,2,3,4],1)
buscar_n_elemento([1,2,3,2,3,4],2)
buscar_n_elemento([1,2,3,2,3,4],3)
buscar_n_elemento([1,2,3,2,3,4],5)
buscar_n_elemento([2,2,2,3,3], 2)
buscar_n_elemento([2,2,2,2,2,3,4,4], 3)
buscar_n_elemento([2,2,2,2,2,3,4,4], 4)

#%%maximo(). versión mejorada

def maximo(lista):
    '''Devuelve el máximo de una lista
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo en el primer valor de la lista
    for e in lista[1:]: # Recorro la lista y voy guardando el mayor
        if e>m:
            m=e        #si e es mayor que m, lo guardo en la variable m
    return m

maximo([1,2,7,2,3,4])
maximo([1,2,3,4])
maximo([-5,4])
maximo([-5,-4])
maximo([2,-3,1])
maximo([-14,50,78,7,16,150,-7,-9,12,23])

#%% minimo

def minimo(lista):
    '''Devuelve el mínimo de una lista
    '''
    m=lista[0]           #inicializo el mínimo en el primer valor de la lista
    for e in lista[1:]:  # Recorro la lista y voy guardando el menor
        if e<m:          
            m=e          #si e es menor que m, lo guardo en la variable m
    return m

minimo([1,2,7,2,3,4])
minimo([1,2,3,4])
minimo([-5,4])
minimo([-5,-4])
minimo([2,-3,1])
minimo([-14,50,78,7,16,150,-7,-9,12,23])
minimo([9,-14,4,78,-45,11,34,-1])
