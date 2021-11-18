# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 12:24:44 2021

@author: Sabri
"""

def trad2s(l):
    '''traduce una lista con 1,0 y -1 
    a una cadena con 'f', 'o' y 'x' '''
    d={1:'f', 0 :'o', -1:'x'}
    s=''.join([d[c] for c in l])
    return s

def trad2l(ps):
    '''traduce cadena con 'f', 'o' y 'x'
    a una lista con 1,0 y -1'''
    inv_d={'f':1, 'o':0, 'x':-1}
    l = [inv_d[c] for c in ps]
    return l

def propagar(l, debug = True):
    s = trad2s(l)
    if debug:
        print(s)#, end = ' -> ')
    W=s.split('x')
    PW=[w if ('f' not in w) else 'f'*len(w) for w in W]
    ps='x'.join(PW)
    if debug:
        print(ps)
    return trad2l(ps)

#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
lp = propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)

#%%
#¿Porqué se acorta la lista?
#Porque no se volvio a agregar los elementos 'x'

#¿Podés corregir el error agregando un solo caracter al código?
#Agrego el termino 'x' en ps='x'.join(PW)

#¿Te parece que este algoritmo es cuadrático como el Ejercicio 6.1 o lineal 
#como el Ejercicio 6.2?
#En cada funcion hace n pasos, termina con 3*n pasos