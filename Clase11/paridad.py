# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 02:11:55 2021

@author: Sabri
"""
# 5 4 3 2 1
# 1 impar
# 2 par
# 3 impar
# 4 par
# 5 impar
#paridad.py

#Escribir dos funciones mutualmente recursiva
#par(n) impar(n) que determine la paridad de un número
#natural dado, usando que:  es impar, un numero mayor
#que 1 es impar si su antecesor es par

def impar(n):
    '''Precondición: Recibe un número natural.
    Devuelve True o False según el numero ingresado sea
    impar
    '''
    if n ==  1:
        return True
    else:
        return par(n - 1)
    
    
def par(n):
    '''Precondición: Recibe un número natural.
    Devuelve True o False según el numero ingresado sea
    par
    '''
    if n == 1:
        return not impar(n)
    else:
        
        return impar(n - 1)

        