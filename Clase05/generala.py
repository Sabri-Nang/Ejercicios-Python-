# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 23:33:29 2021

@author: Sabri
"""
import random
from collections import Counter

def tirar(n=5):
    '''Devuelve una lista con 5 valores aleatorios
    del 1 al 6'''
    tirada = []
    for i in range(n):
        tirada.append(random.randint(1,6))   #Agrega a la lista un valor random del
                                           #1 al 6
    return tirada
    
def es_generala(tirada):
    '''Devuelve True si y sólo si los cinco dados de la lista tirada son iguales'''
    return max(tirada)==min(tirada)

def generala(dejo_un_dado=False):
    '''Devuelve True o False en caso de haber obtenido o no generala en una partida.
    Cada partida tiene hasta 3 tiradas.
    El parámetro dejo_un_dado indica si al salir números diferentes en cada dado
    se vuelven a tirar todos (dejo_un_dado=False) o se deja un dado en la mesa
    (dejo_un_dado=True)'''
    dados = 5
    tirada = tirar(dados)
    #print(tirada)
    j = 0
    generala = es_generala(tirada)
    #if not es_generala(tirada):   
    while (generala==False and j<2):
        
        if len(Counter(tirada).most_common())==5:  #Counter(tirada).most_common() es una lista de tuplas
                                                   #del tipo (numero que salio, cantidad de dados en los que salió)
            
            dejo_dados = dejo_un_dado   #Dejo_dado guarda el valor de dejo_un_dado.
                                      #Si todos son diferentes uso ese valor
                                      
        else:
            dejo_dados = True           #Si no siempre dejo dados.
    
#Observación: puse la variable dejo_dados porque si utilizaba en la primer
#tirada ese valor luego necesariamente debía cambiarlo a True para llenar la lista mesa.
#Pero si lo cambio a True y en la segunda tirada salen todos distintos ya no 
#cumpliría que no se deje un dado      
        
            
        if dejo_dados:
            numero_veces = Counter(tirada).most_common()[0] #cuento las veces que salió cada número, 
                                                          #ordenados por el que mas salió
                                                          #Tomo la primera tupla cuyos valores son:
                                                          #(numero que más salió, cantidad de dados en los que salió)
            mesa = [numero_veces[0]] * numero_veces[1]   #Armo una lista con los dados 
                                                     #que dejo en la mesa
        else:
            mesa = []
        
        
        dados_a_tirar = 5 - len(mesa)                #cantidad de dados que quedan por tirar
        tirada = tirar(dados_a_tirar)
        tirada.extend(mesa)
        #print(tirada)
        j += 1
        generala = es_generala(tirada)

    return generala


#%%          
    
    

N = 10**7
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

prob_teorica=6**-4
print(f'La probabilidad teórica es: {prob_teorica}')

#%%
import datetime

hora_inicio=datetime.datetime.now()

N = 10**6
G = sum([generala() for i in range(N)])
prob = G/N
print(f'\nJugué {N} veces, de las cuales {G} formé generala.')
print(f'Podemos estimar la probabilidad de sacar generala sin dejar un dado cuando salen diferentes como: {prob:.6f}.')

G = sum([generala(True) for i in range(N)])
prob = G/N
print(f'\nJugué {N} veces, de las cuales {G} formé generala.')
print(f'Podemos estimar la probabilidad de sacar generala sin dejar un dado cuando salen diferentes como: {prob:.6f}.')

hora_final=datetime.datetime.now()
delta_hora=hora_final-hora_inicio

print(f'Tardo {delta_hora} en finalizar')
