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

#%% Búsqueda lineal ordenada

def busqueda_lineal_lordenada(lista,e):
    '''Recibe una lista ordenada de menor a mayor y un elemento e.
    Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z>e:
            break
        elif z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

#%% Búsqueda binaria

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria.
    Precondición: la lista está ordenada.
    Devuelve una tupla cuyo primer elemento es -1 si x no está en la lista
    o p tal que lista[p] == x si x está en la lista. Y su segundo elemento
    es la cantidad de comparaciones que realizó.
    '''
    if verbose:
        print(f'[DEBUG] izq | der | medio')
    pos = -1 #Inicializo respues, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comps = 0
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
        comps += 1
    return pos, comps

#%% donde insertar
def donde_insertar(lista, x):
    '''Recibe una lista ordenada y un elemento y devuelve
    la posición de ese elemento en la lista, si se encuenta
    o la posición donde se podría insertar para que
    permanezca ordenada'''
   
    
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

#%%Contar cantidad de apariciones - Gráficos de complejidad

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

    
