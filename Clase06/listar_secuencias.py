# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 15:12:49 2021

@author: Sabri
"""

def incrementar(s):
    '''Recibe una lista binaria y devuelve la lista
    correspondiente a siguiente número en binarios
    '''
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s

#Tiene una complejidad n

def listar_secuencias(n):
    '''Devuelve una lista con todas las secuencias de longitud
    n comenzando con ([0]*n) y usa en cada paso la función incrementar()
    '''
    s = [0]*n
    secuencia = []
    secuencia.append(s.copy())
    while (s != [1]*n):      
        s = incrementar(s)
        secuencia.append(s.copy())
        #print(s)
    return secuencia

#Hay 2^n secuencias de longitud n y 2^(n+1) secuencias de longutud n+1
#%%

import timeit

starttime = timeit.default_timer()
listar_secuencias(15)
print("The time difference is :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
listar_secuencias(20)
print("The time difference is :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
listar_secuencias(22)
print("The time difference is :", timeit.default_timer() - starttime)

#Notar que tarda muchísimo cuando en listar_secuencia se habilita print(s)
#Para n = 15 tarda 0.1416112000006251
#Para n = 20 tarda 6.606935899995733
#Para n = 25 tarda
