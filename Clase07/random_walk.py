# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 00:04:08 2021

@author: Sabri
"""

import numpy as np
import matplotlib.pyplot as plt
#import random


#random.seed(10)
np.random.seed(2325)

def randomwalk(largo):
    pasos=np.random.randint(-1,2,largo)    
    return pasos.cumsum()

N = 100000
caminatas = []


fig = plt.figure()
plt.subplot(2, 1, 1)
for i in range(12):
    caminata = randomwalk(N)
    caminatas.append(caminata)   #guardo las 12 caminatas en una lista
    plt.plot(caminata)      
plt.xticks([]), plt.yticks([-500, 0, 500])    
plt.ylim(-1000, 1000)
plt.title('12 Caminatas al azar')

maximos = {abs(caminata).max(): caminata for caminata in caminatas}  #diccionario, clave: cuanto se alejo, valor:caminata
maximos_sort = sorted(maximos.items())    #ordeno desde la caminata que menos se aleja
                                          #a la que mas se aleja. (lista de tuplas-> (distancia, caminata))


plt.subplot(2, 2, 3)
plt.plot(maximos_sort[11][1])
plt.xticks([]), plt.yticks([-500, 0, 500])
plt.ylim(-1000, 1000)
plt.title('La caminata que más se aleja')

plt.subplot(2, 2, 4)
plt.plot(maximos_sort[0][1])
plt.xticks([]), plt.yticks([-500, 0, 500])
plt.ylim(-1000, 1000)
plt.title('La caminata que menos se aleja')
plt.show()

# plt.figure(2)
# plt.plot(maximos_sort[11][1])
# plt.xticks([]), plt.yticks([-500, 0, 500])
# plt.ylim(-1000, 1000)
# plt.title('La caminata que más se aleja')
# plt.show()

# plt.figure(3)
# plt.plot(maximos_sort[0][1])
# plt.xticks([]), plt.yticks([-500, 0, 500])
# plt.ylim(-1000, 1000)
# plt.title('La caminata que menos se aleja')
# plt.show()
