# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:56:13 2021

@author: Sabri
"""


def valor_absoluto(n):
    '''
    Devuelve el valor absoluto de n.
    Pre: Recibe un número.
    Pos: Devuelve el valor absoluto del número ingresado.
    '''
    if n >= 0:
        return n
    else:
        return -n
    
#%%   

def suma_pares(l):
    '''
    Suma los valores pares de una lista ingresada. 
    Devuelve la suma si existen valores pares en la lista,
    de lo contrario devuelve 0.
    
    Pre: Recibe una lista de números.
    Pos: Devuelve la suma de los valores pares de la lista
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

# res invariante de ciclo
#%%

def veces(a, b):
    '''
    Calcula b veces el valor a.
    
    Pre: Recibe dos valores, b debe ser un número natural o cero.
    Pos: Devuelve b veces el valor a.
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1   
    return res

# res, nb invariantes de ciclo

#%%

def collatz(n):
    '''
    Pre: Recibe un número mayor que cero entero.
    Pos: Devuelve la cantidad de iteraciones desde n
    para alcanzar 1 siguiendo la conjetura de Collatz
    '''
    res = 1
    #secuencia = []
    #secuencia.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        #secuencia.append(n)
        res += 1

    return res #, secuencia

# res invariante de ciclo.
