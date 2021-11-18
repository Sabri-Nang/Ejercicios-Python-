# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 02:39:53 2021

@author: Sabri
"""

#maximo.py
#Escribir una función que encuentre el mayor elemento
#de una lista sin usar max()

#[1, 2, 3, 4, 5]
# def maximo(lista):
#     if len(lista) == 1:
#         res = lista[0]
#     else:
#         primero = lista[0]
#         max_del_resto = maximo(lista[1::])
#         res = max(primero, max_del_resto)
        
#     return res


def maximo(lista):
    '''Precondición: ingresar una lista de números
    Devuelve el máximo valor de la lista
    '''
    cLista = lista.copy()
    if len(cLista) == 1:
        return cLista[0]
    elif len(cLista) == 2:
        if cLista[0] >= cLista[1]:
            return cLista[0]
        else:
            return cLista[1]
    else:
        nlista = [cLista[-1], cLista[-2]]
        if nlista[0] >= nlista[1]:
            #maxim = nlista[0]            
            cLista.remove(nlista[1]) #remuevo los mas chicos dela lista
            
        else:
            #maxim = nlista[1]
            cLista.remove(nlista[0])
        #maxim = maximo(cLista)
        

        return maximo(cLista)

 
lista1 = [1, 2, 3, 4]
lista2 = [4, 3, 2, 1]
lista3 = [10, 9, 99, 25]       
lista4 = [10, 0.1, 258, 789, 1047, 11, -87]    
lista5 = [125, 14]
lista6 = [0]   
    