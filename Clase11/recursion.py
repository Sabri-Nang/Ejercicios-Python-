# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:56:06 2021

@author: Sabri
"""

def sumar(a, b):
    '''Pre b>=0
    '''
    print(f'Llame a sumar con {a} {b}')
    if b == 0:
        res = a
    else:
        res = sumar(a+1, b-1)
    print(f'El resultado de sumar {a} con {b} es {res}')
    return res

def factorial(n):
    if n == 1:
        res = 1
    else:
        res = n * factorial(n-1)
    return res

#otra forma de hacer el factorial
def factorial(n):
    '''Precondicion: n entero positivo.
    Devuelve: n!'''
    if n == 1:
        return 1
    return n * factorial(n - 1)

def es_impar(n, str_tab = ''):
    if n == 0:
        print(f'{str_tab} Llegue al cero')
        res = False
    else:
        print(f"{str_tab} Para saber si {n} es impar, niego la paridad de uno menos")
        temp = es_impar(n-1, str_tab + '\t')
        res = not temp
        print(f'{str_tab} Para saber si {n} obtive es_impar({n-1})={temp} y lo negue para obtener {res}')
    return res

def maximo(lista):
    if len(lista) == 1:
        res = lista[0]
    else:
        primero = lista[0]
        max_del_resto = maximo(lista[1::])
        res = max(primero, max_del_resto)
        
    return res

lista_ejemplo = [2, 0, 6, 4]
maximo(lista_ejemplo)

def permutaciones(lista):
    if len(lista) == 0:
        res = []
    elif len(lista) == 1:
        res = [lista]
    else:
        res = []
        for idx, elem in enumerate(lista):
            
            permut_resto = permutaciones(lista[:idx] + lista[idx+1:]) #tiene todos los valores menos el idx
            res += [[elem] + p for p in permut_resto]
    return res
