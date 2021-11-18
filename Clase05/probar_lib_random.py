# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:23:56 2021

@author: Sabri
"""

import random

tirada=[]
for i in range(5):
    tirada.append(random.randint(1,6))
  
# poner _ es una variable muda. Podria poner
#i
tirada=[random.randint(1,6) for _ in range(5)]

