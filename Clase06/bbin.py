# -*- coding: utf-8 -*-
"""
Created on Tues Apr  20 02:29:42 2021

@author: Sabri
"""

#%% Búsqueda binaria

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria.
    Precondición: la lista está ordenada.
    Devuelve -1 si x no está en la lista;
    Devuelve p tal que lista[p] == x, si x está en la lista. 
    '''
    if verbose:
        print('[DEBUG] izq | der | medio')
    pos = -1 #Inicializo respues, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq<=der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} | {der:>3d} | {medio:3d}')
        if lista[medio] == x:
            pos = medio   #elemento encontrado!
        if lista[medio] > x:
            der = medio-1 #descarto la mitad derecha
        else:             #if lista[medio] < x :
            izq = medio + 1 #descarto mitad izquierda
    return pos

#%%

def donde_insertar(lista, x):
    '''Recibe una lista ordenada y un elemento y devuelve
    la posición de ese elemento en la lista, si se encuenta
    o la posición donde se podría insertar para que
    permanezca ordenada'''
   
    4
    izq = 0
    der = len(lista) - 1
    while izq<=der:
        medio = (izq + der) // 2
        
        if lista[medio] == x:
            pos = medio   #elemento encontrado!
            return pos
        if lista[medio] > x:
            der = medio - 1 #descarto la mitad derecha
            pos = medio
        else:             #if lista[medio] < x :
            izq = medio + 1 #descarto mitad izquierda
            pos = medio + 1 

    return pos

#%%

def insertar(lista, x):
    '''Recibe una lista y un elemento x, si el elemento se
    encuentra en la lista devuelve su posición. Si no se 
    encuentra en la lista lo inserta en la posición correcta.
    '''
    index = donde_insertar(lista, x)
    if lista[index] == x:
        return index
    else:
        lista.insert(index,x)
        return index, lista
#%%
donde_insertar([1,2,4,5], 3)
insertar([1,2,4,5], 3)
    
