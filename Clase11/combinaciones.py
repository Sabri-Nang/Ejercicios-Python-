# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 04:44:02 2021

@author: Sabri
"""

#combinaciones.py
#Escribir una función recursiva que reciba una lista
#de caracteres únicos, y un número k, e imprima todas las posibles cadenas
#de longitud k formadas con los caracteres dados 
#(permitiendo caracteres repetidos)


# def combinaciones(lista, k):
#     #cadena = lista
#     #res = ''
#     if len(lista) == 0:
#         res = ''
#     elif k == 1:
#         for i in lista:
#             res = i + ' '
#     else:
#         res = ' '
#         i = 1
#         while i <=k:
#             res += combinaciones(lista, i)
#             i += 1

#     return res

def combinaciones(lista, n):
    """
    Recibe una lista de caracteres unicos,
    y un numero k, e imprime todas las posibles
    cadenas de longitud k formadas con los caracteres dados
    (permitiendo caracteres repetidos).
    Ejemplo: combinaciones(['a', 'b', 'c'], 2) -> aa ab ac ba bb bc ca cb cc
    """
    if n == 1:
        return lista
    #return [i + j for i in lista for j in combinaciones(lista, n-1)]
    lista_combinaciones = []
    
    for i in lista:
        for j in combinaciones(lista, n - 1):
            lista_combinaciones.append(i + j)
    return lista_combinaciones
    
        
combinaciones(['a', 'b'], 3)
