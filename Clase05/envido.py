# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 05:12:58 2021

@author: Sabri
"""
import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

random.sample(naipes,k=3)

#mezclar naipes
random.shuffle(naipes)

#tres ultimas cartas
naipes[-3:]

n1 = naipes.pop()
n2 = naipes.pop()
n3 = naipes.pop()

print(f'Repartí el {n1[0]} de {n1[1]}, el {n2[0]} de {n2[1]} y el {n3[0]} de {n3[1]}. Quedan {len(naipes)} naipes en el mazo.')