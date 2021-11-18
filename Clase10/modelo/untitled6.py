# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 21:37:56 2021

@author: Sabri
"""

from animal import Animal, Leon, Antilope
from mundo import Mundo
from tablero import Tablero

L = Leon()
L.energia
L.edad
L.es_leon()
L.es_antilope()
L.pasar_un_ciclo()
L.energia
L.edad
L.tiene_hambre()

A1 = Antilope()
A2 = Antilope()
A1.energia
A1.edad
A1.es_antilope()

vecinos = [(1, A1), (2, A2)]
pos = L.alimentarse(vecinos)

if pos:
    print(f'El león se come al antílope A{pos}')
else:
    print('El león no come')

M = Leon()
M.puede_reproducir()
M.pasar_un_ciclo()
M.puede_reproducir()    

vecinos = [L]
lugares_libres = [4, 5, 6, 7, 8]
L.puede_reproducir()
M.puede_reproducir()

pos = M.reproducirse(vecinos, lugares_libres)
print(f'Nace un nuevo leoncito en la posición {pos}')
M.puede_reproducir()
M.pasar_un_ciclo()
M.puede_reproducir()    

#%%
m = Mundo(12, 6, 5, 15, debug=True)

import time
for i in range(20):
    m.pasar_un_ciclo()
    time.sleep(2)
    print(i +1)
    print(m)    