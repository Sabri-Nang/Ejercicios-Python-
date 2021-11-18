# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 01:07:05 2021

@author: Sabri
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def crear_album(figus_total): 
    '''Recibe un int figus_total.
    Devuelve un álbum (vector de ceros) con figus_total espacios 
    para pegar figuritas
    '''    
    return np.zeros(figus_total, int)

def album_incompleto(album):
    '''
    Recibe un vector album.
    Devuelve True si el álbum está incompleto y False si está completo
    '''
    return 0 in album

def comprar_figu(figus_total):
    '''Recibe el número total de figuritas que tiene el álbum (dado por el parámetro 
    figus_total).
    Devuelve un número entero aleatorio que representa la figurita que nos tocó.
    '''
    return random.randint(0, figus_total-1)

def comprar_paquete(figus_total, figus_paquete):
    '''Recibe el total de figuritas del álbum y la cantidad de figuritas por paquete.
    Devuelve una lista con números enteros aleatorios que representan las figuritas
    del paquete.
    '''
    paquete = random.choices(np.arange(figus_total), k=figus_paquete)
    return paquete
    

def cuantas_figus(figus_total):
    '''Recibe el tamaño del álbum, int figus_total.
    Devuelve la cantidad de figuritas que se debieron comprar para completarlo
    '''
    album = crear_album(figus_total)
    incompleto = album_incompleto(album)
    figuritas = 0
    while incompleto:
        figu = comprar_figu(figus_total)
        album[figu] += 1
        figuritas += 1
        incompleto = album_incompleto(album)
    return figuritas

def cuantos_paquetes(figus_total, figus_paquete):
    '''Recibe el tamaño del álbum, int figus_total.
    Devuelve la cantidad de paquetes que se debieron comprar para completarlo.
    '''
    album = crear_album(figus_total)
    incompleto = album_incompleto(album)
    paquetes = 0
    while incompleto:
        figus = comprar_paquete(figus_total, figus_paquete)
        paquetes += 1
        for figu in figus:
            album[figu] += 1
        incompleto = album_incompleto(album)
    return paquetes


#%% Ejercicio 5.13

n_repeticiones = 1000
figus_total = 6
figus_compradas = [cuantas_figus(figus_total) for _ in range(n_repeticiones) ]
promedio = np.mean(figus_compradas)
print(f'\nPara llenar un álbum de {figus_total} figuritas se necesita comprar en promedio {int(promedio)} figuritas')  
        
#%% Ejercicio 5.14

n_repeticiones = 1000
figus_total = 670
figus_compradas = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
promedio = np.mean(figus_compradas)
print(f'\nPara llenar un álbum de {figus_total} figuritas se necesita comprar en promedio {int(promedio)} figuritas')  

#%% Ejercicio 5.18

n_repeticiones = 100
figus_total = 670
figus_paquete = 5
paquetes_comprados = [cuantos_paquetes(figus_total, figus_paquete) 
                      for _ in range(n_repeticiones)]
promedio = np.mean(paquetes_comprados)
print(f'\nPara llenar un álbum de {figus_total} figuritas se necesita comprar en promedio {int(promedio)} paquetes de figuritas')  

#%%

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()

#%% Ejercicio 5.19. Estimar la probabilidad de completar un álbum con 850 paquetes
#o menos

n_repeticiones = 1000
figus_total = 670
figus_paquete = 5
paquetes_comprados = [cuantos_paquetes(figus_total, figus_paquete) 
                      for _ in range(n_repeticiones)]
n_paquetes_hasta_llenar = np.array(paquetes_comprados)
probabilidad = (n_paquetes_hasta_llenar<=850).sum() / 1000
print(f'\nLa probabilidad de llenar un álbum comprando 850 paquetes o menos es de {probabilidad:.2%}')

# Ejercicio 5.20. Plotear histograma

plt.hist(paquetes_comprados, bins=25)

#Ejercicio 5.21. Estimá cuántos paquetes habría que comprar para tener una 
#chance del 90% de completar el álbum

#prob*CantidadDeExperimentos=0.90*1000=900=suma(paquetes_comprados)

lista_prob_90 = []
for i in range(min(n_paquetes_hasta_llenar), max(n_paquetes_hasta_llenar)+1):
    #recorro el rango de paquetes
    if ((n_paquetes_hasta_llenar<=i).sum())/n_paquetes_hasta_llenar.size==0.9:
        #me fijo cual es la probabilidad para cada una de la cantidad de paquetes posibles
        #y tomo solo los que la prob me da 0.9
        lista_prob_90.append(i)
lista_prob_90 = np.array(lista_prob_90)
#print(lista_prob_90)
promedio_prob_90 = lista_prob_90.mean()
print(f'''Para tener un 90% de probabilidad de llenar el álbum se necesita comprar 
en promedio {promedio_prob_90} paquetes de figuritas''')

#Ejercicio 5.22. No se repiten las figuritas en los paquetes
#Propuesta:
#Usar paquete= random.sample(np.arange(figus_total), k=figus_paquete) 
#en la función comprar_paquete en lugar de
#paquete = random.choices(np.arange(figus_total), k=figus_paquete)
#y ejecutar todo de nuevo
#%%

'''Ejercicio 5.23: Cooperar vs competir.
cinco amigues se juntan y deciden compartir la compra de figuritas y 
el llenado de sus cinco álbumes solidariamente. Calculá cuántos paquetes 
deberían comprar si deben completar todos. Hacé 100 repeticiones y compará 
el resultado con la compra individual que calculaste antes.
Propuesta:
Generar 5 álbumes vacíos.
Empezar llenando un álbum, en el caso de que la figurita salida en el paquete
ya esté en el álbum, ponerla en el álbum siguiente.
Me voy fijando la figurita que sale, si esta en un álbum paso al siguiente...
Así hasta llenar los 5
Para eso voy armando una matriz de 5 x n_figus y al final la matriz no debe tener 
ceros
'''
def cuantos_paquetes_cooperar(figus_total, figus_paquete):
    '''Recibe el tamaño del álbum, int figus_total.
    Devuelve la cantidad de paquetes que se debieron comprar para completar
    cinco álbumes.
    '''
    albumes = [crear_album(figus_total) for i in range(5)]
    albumes = np.array(albumes)        #Cada fila es un album, cada columna misma figurita
    incompletos = album_incompleto(albumes)
    paquetes = 0
    while incompletos:
        figus = comprar_paquete(figus_total, figus_paquete)
        paquetes += 1
        for figu in figus:
            i = 0
            while i<5:
                if albumes[i, figu]==0:
                    albumes[i, figu] += 1
                    break
                else:
                    i += 1
        incompletos = album_incompleto(albumes)
    return paquetes   


n_repeticiones = 100
figus_total = 670
figus_paquete = 5
paquetes_comprados = [cuantos_paquetes_cooperar(figus_total, figus_paquete) 
                      for _ in range(n_repeticiones)]
promedio = np.mean(paquetes_comprados)
print(f'\nPara llenar 5 álbumes de {figus_total} figuritas se necesita comprar en promedio {int(promedio)} paquetes de figuritas')  

#Se logra llenar los 5 álbumes con en promedio 2000 paquetes
#Con aproximadamente el doble de paquetes que necesito para llenar uno, lleno 5
#álbumes. Cada amigue debe comprar aprox 400 paquetes para que les 5 llenen el álbum,
#en comparación con los aprox 950 paquetes que deben comprar si no cooperan     

