# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:24:43 2021

@author: Sabri
"""

#Ejercicio 6.1. Propagar por vecino

def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1 and l[i+1]==0:
            l[i+1] = 1
            modif = True
        if e==1 and i>0 and l[i-1]==0:
            l[i-1] = 1
            modif = True
        
    return modif

def propagar(l):
    m = l.copy()
    veces=0
    while propagar_al_vecino(l):
        veces += 1

    print(f"Repetí {veces} veces la función propagar_al_vecino.")
    print(f"Con input {m}")    
    print(f"Y obtuve  {l}")
    return m
#%%
propagar([0,0,0,0,1])
propagar([0,0,1,0,0])
propagar([1,0,0,0,0])

#La función propagar realiza en el peor de los casos: n^2 operaciones

#¿Por qué los tests l[i+1]==0 y l[i-1]==0 de la función propagar_al_vecino 
#no causan un IndexError en los bordes de la lista?
#Porque se excluyen los bordes al poner i<n-1 == i<l-1. O sea que llega hasta
#l-2. Del otro lado esta i>0, o sea q funciona desde i=1

#¿Por qué propagar([0,0,0,0,1]) y propagar([1,0,0,0,0]), siendo entradas 
#perfectamente simétricas, no generan la misma cantidad de repeticiones de 
#llamadas a la función propagar_al_vecino?
#Porque la funcion propagar_al_vecino hace un for desde i=0, si todos son ceros
#y el ultimo es 1 debe pasar por todos los ceros anteriores.
#En cambio si comienza con 1 en el primer paso propaga a derecha, luego en 
#solo una vez ejecutada la funcion propaga_al_vecino, ya propaga toda la lista

#Sobre la complejidad. Si te sale, calculá:
#¿Cuántas veces como máximo se puede repetir el ciclo while en una lista de 
#largo n?
#¿Cuántas operaciones hace "propagar_al_vecino" en una lista de largo n?
#Entonces, ¿cuántas operaciones hace como máximo esta versión de propagar 
#en una lista de largo n? ¿Es un algoritmo de complejidad lineal o cuadrática?
#Se puede repetir n-1 veces.
#propaga_al_vecino hace como maximo n-1 operaciones.
#Es un algoritmo de complejidad cuadratica
