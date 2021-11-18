# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 08:59:11 2021

@author: Sabri
"""

def med_hoja(n):
    '''Recibe n natural o cero.
    Devuelve el tamaño en mm de una hoja An según
    las normas ISO 216
    '''
    def med_hoja_aux(n, lista_hojas):
        if len(lista_hojas) - 1 == n:
            return lista_hojas
        else:
            i = len(lista_hojas) - 1
            ancho = lista_hojas[i][0]
            largo = lista_hojas[i][1]
            hoja_sig = (largo//2, ancho)
            lista_hojas.append(hoja_sig)
            med_hoja_aux(n, lista_hojas)
        return lista_hojas
            
    lista_hojas = [(841, 1189)]
    lista_hojas = med_hoja_aux(n, lista_hojas)
    ancho = lista_hojas[len(lista_hojas)-1][0]
    largo = lista_hojas[len(lista_hojas)-1][1]
    return f'({ancho} x {largo} mm)'

med_hoja(0)
