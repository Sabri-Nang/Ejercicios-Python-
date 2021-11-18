# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 23:33:29 2021

@author: Sabri
"""
import random

def tirar(n=5):
    '''Devuelve una lista con 5 valores aleatorios
    del 1 al 6'''
    tirada=[]
    for i in range(n):
        tirada.append(random.randint(1,6))   #Agrega a la lista un valor random del
                                           #1 al 6
    return tirada
    
def es_generala(tirada):
    '''Devuelve True si y sólo si los cinco dados de la lista tirada son iguales'''
    return max(tirada)==min(tirada)


    
    
N = 10**6
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

prob_teorica=6**-4
print(f'La probabilidad teórica es: {prob_teorica}')