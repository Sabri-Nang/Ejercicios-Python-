# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:49:27 2021

@author: Sabri
"""
#Ejercicio 6.2: Propagar como el auto fantastico
def propagar_a_derecha(l):
    lista = l.copy()
    n = len(lista)
    for i,e in enumerate(lista):
        if e==1 and i<n-1:
            if lista[i+1]==0:
                lista[i+1] = 1
    return lista
#%
def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1]
#%
def propagar(l):
    
    ld=propagar_a_derecha(l)
    lp=propagar_a_izquierda(ld)
    return lp
#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
print("Estado original:  ",l)
print("Porpagando...")
lp=propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)

#%% Preguntas
#¿Por qué se modificó la lista original?
#Porque ld hace referencia a l. En las funciones propagar_a_derecha y propagar_a_izquierda
#se esta modificando la lista y, y ld llama a esa referencia.

#¿Por qué no quedó igual al estado propagado?
#Porque antes de salir ejecuta propagar_a_izquierda, esta funcion no hace modificaciones
#sobre la lista l sino que hace una copia y devuelve esa copia modificada

#Corregí el código para que no cambie la lista de entrada. 
#agrego lista = l.copy() en la funcion propagar_a_derecha(l) y cambio l por lista

#¿Cuántas operaciones hace como máximo propagar_a_derecha en una lista de largo n?
#Hace como maximo n operaciones

#Sabiendo que invertir una lista ([::-1]) requiere una cantidad lineal de 
#operaciones en la longitud de la lista ¿Cuántas operaciones hace como máximo 
#propagar en una lista de largo n?
#Hace como maximo 2*n operaciones
