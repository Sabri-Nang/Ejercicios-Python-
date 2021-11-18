# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 02:49:41 2021

@author: Sabri
"""

import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

def calcular_pi():
    N = 10**7
    M = 0
    puntos=[generar_punto() for _ in range(N)]
      
    for punto in puntos:
        if (punto[0]**2 + punto[1]**2)<=1:
            M += 1
    pi = M * 4 / N
    
    return pi

pi = calcular_pi()