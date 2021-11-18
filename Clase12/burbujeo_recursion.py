# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 20:12:04 2021

@author: Sabri
"""
def ord_burbujeo(lista):
    N = len(lista)
    j = 1
    comparaciones = 0
    while j < N:
        i = 1
        comparaciones += j
        while i < len(lista):
            #comparaciones += i
            if lista[i-1] > lista[i]:
                aux = lista[i]
                lista[i] = lista[i - 1]
                lista[i - 1] = aux
            
            i += 1
        j += 1
    return comparaciones

#%%
#visto por un compa en clase
def ord_burbujeo_rec(lista):
    comparaciones = 0
    if len(lista) <= 1:
        return lista, comparaciones
    else:
        for i in range(len(lista) - 1):
            comparaciones += i + 1
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                n = len(lista) - 1
                lista[:n], comp= ord_burbujeo_rec(lista[:n])
                

        return lista, comparaciones
        


lista = [51, 967, 243, 732, 442, 163, 871, 903, 916, 868]
ord_burbujeo_rec(lista)
lista = [51, 967, 243, 732, 442, 163, 871, 903, 916, 868]
ord_burbujeo(lista)

      
lista_1 = [1, 2, -3, 8, 1, 5]
ord_burbujeo_rec(lista_1)
lista_1 = [1, 2, -3, 8, 1, 5]
ord_burbujeo(lista_1)
lista_2 = [1, 2, 3, 4, 5]
lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
lista_4 = [10, 8, 6, 2, -2, -5]
lista_5 = [2, 5, 1, 0]
