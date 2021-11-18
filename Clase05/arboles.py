# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 17:02:48 2021

@author: Sabri
"""
import csv
from collections import Counter
import os
import matplotlib.pyplot as plt
import numpy as np
import random

def leer_parque(nombre_archivo, parque):
    '''Abre un archivo y devuelve una lista de diccionarios con todos los
    datos por cada árbol del parque elegido'''
    lista_arboles=[]
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        rows=csv.reader(f)
        headers=next(rows)
        for n_row, row in enumerate(rows, start=1):
            arbol=dict(zip(headers,row))
            arbol['altura_tot']=float(arbol['altura_tot'])
            if parque==arbol['espacio_ve']:
                lista_arboles.append(arbol)
    return lista_arboles

           
def especies(lista_arboles):
    '''Dada una lista de arboles, devuelve una lista con las especies
    diferentes'''
    especies=[]
    for arbol in lista_arboles:
        especie = arbol['nombre_com']
        especies.append(especie)
    especie = set(especies)
    especie = list(especie)
    return especie



def contar_ejemplares(lista_arboles):
    ejemplares=Counter()
    for arbol in lista_arboles:
        ejemplares[arbol['nombre_com']]+=1
    return ejemplares



def especies_mas_frecuentes(nombre_archivo, lista_parques):
    '''Dado tres parques informa las 5 especies más frecuentes en cada
    parque'''
    
    resultado={}
    for parque in lista_parques:
        
        lista_arboles=leer_parque(nombre_archivo, parque)
        ejemplares=contar_ejemplares(lista_arboles)
        ejemplares=ejemplares.most_common(5)
        resultado[parque]=ejemplares
        print(f'\nEspecies más comunes en el parque {parque}:')
        for ejemplar in ejemplares:
            print(f'{ejemplar[0]}: {ejemplar[1]}')
    return resultado
    
def obtener_alturas(lista_arboles, especie):
    '''Dada una lista de arboles y una especie devuelve una lista con las alturas
    de los ejemplares de esa especie en la lista'''
    alturas=[]
    for arbol in lista_arboles:   
        if especie in arbol['nombre_com']: 
            altura=arbol['altura_tot']    
            alturas.append(altura)
    return alturas

def obtener_inclinaciones(lista_arboles, especie):
    '''Dada una lista de arboles y una especie devuelve una lista con 
    las inclinaciones de dicha especie'''
    inclinaciones=[]
    for arbol in lista_arboles:
        if especie in arbol['nombre_com']:
            inclinacion=arbol['inclinacio']
            inclinaciones.append(float(inclinacion))
    return inclinaciones

def especimen_mas_inclinado(lista_arboles):
    '''Dada una lista de árboles devuelve la especie que tiene el ejemplar
    más inclinado y su inclinación en una tupla'''
    espec=especies(lista_arboles)
    especie_inclinacion={}
    
    for especie in espec:
        inclinaciones=obtener_inclinaciones(lista_arboles, especie)
        mas_inclinado=float(max(inclinaciones))
        especie_inclinacion[especie]=mas_inclinado
    inclinacion_especie=list(zip(especie_inclinacion.values(),especie_inclinacion.keys()))
    inclinacion_especie=sorted(inclinacion_especie, reverse=True)
    return (inclinacion_especie[0][1], inclinacion_especie[0][0])

def especie_promedio_mas_inclinada(lista_arboles):
    espec=especies(lista_arboles)
    especie_inclinacion_prom={}
    for especie in espec:
        inclinaciones=obtener_inclinaciones(lista_arboles, especie)
        prom_inclinacion=sum(inclinaciones)/len(inclinaciones)
        especie_inclinacion_prom[especie]=prom_inclinacion
    inclinacion_prom_especie=list(zip(especie_inclinacion_prom.values(), especie_inclinacion_prom.keys()))
    inclinacion_prom_especie=sorted(inclinacion_prom_especie, reverse=True)
    return (inclinacion_prom_especie[0][1], inclinacion_prom_especie[0][0])
    
def leer_arboles(nombre_archivo):
    '''Abre un archivo y devuelve una lista de diccionarios con todos los
    datos por cada árbol'''
    #arboleda=[]
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        rows=csv.reader(f)
        headers=next(rows)
        types=[float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float]
        arboleda=[{name:func(val) for name, func, val in zip(headers, types, row)} for row in rows]
    return arboleda

def medidas_de_especies(especies, arboleda):
    '''Recibe una lista de especies y una lista de diccionarios de arboles y
    devuelve un diccionario cuyas claves son las especies y sus valores son
    listas de tuplas (altura, diametro)'''
    medidas={especie:[(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda
                   if arbol['nombre_com']==especie] for especie in especies}
    return medidas
        
def graficar_histograma_alturas(arboleda, especie):
    '''Recibe una lista de diccionarios de árboles y una especie.
    Realiza un histograma de las alturas de los árboles de esa especie de la 
    lista ingresada
    '''
    
    altos = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com']== especie]
    plt.figure()
    plt.hist(altos, bins=50)
    plt.xlabel('Altura (m)')
    plt.ylabel('cantidad de árboles')
    plt.title(f'Histograma de alturas de la especie {especie}')
    
    
def graficar_especies_alt_diam(arboleda, especies, juntos=True):
    '''Recibe un archivo csv y una lista de especies.
    Realiza un gráfico de altura vs diámetro por cada especie
    Parámetro juntos determina si grafica todo en un gráfico o en gráficos
    distintos. Por defecto es True
    '''
    
    medidas= medidas_de_especies(especies, arboleda)
    for i, nombre in enumerate(medidas):  #recorro la lista de diccionarios
        #colores = ['aqua', 'magenta', 'salmon']
        altura = [h for h, d in medidas[nombre]]
        diam = [d for h, d in medidas[nombre]]
        if not juntos:
            plt.figure()
            plt.title(f'Relación diámetro-alto para {nombre}')
        else:
            plt.title('Relación diámetro-alto para distintas especies')
        colores = (round(random.random(),2), round(random.random(),2), round(random.random(),2))
        plt.scatter(diam, altura, alpha=0.5, label=nombre, s=10, color=colores)
        #Los colores son random con rgb            
        plt.xlabel('Diámetro (cm)')
        plt.ylabel('Alto (m)')
        
        #plt.xlim(0,300)
        #plt.ylim(0,60)
        plt.legend()
        plt.grid(True)
    
        
        

#%% Probar funcion lista_arboles

# import os

# #Si se ejecuta desde un directorio ../ejercicios_python/Clase0x
# #y Data en ejercicios_python
# mycwd=os.getcwd()    #directorio en el cual estoy
# os.chdir('..')
# path=os.getcwd()

# arbolado_path='Data/arbolado-en-espacios-verdes.csv'
# nombre_archivo=os.path.join(path, arbolado_path)
# os.chdir(mycwd)



# lista_arboles=leer_parque(nombre_archivo, 'GENERAL PAZ')

# #probar función especies
# especs=especies(lista_arboles)

# #probar función contar_ejemplares
# ejemplares=contar_ejemplares(lista_arboles)

# #probar función especies_mas frecuentes
# parques=['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
# especies_mas_frecuentes('../Data/arbolado-en-espacios-verdes.csv', parques)


# #Probar función obtener alturas
# parques=['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
# especie='Jacarandá'  
 
# for parque in parques:
#     alturas=obtener_alturas(leer_parque(nombre_archivo, parque), especie)        
#     altura_max=max(alturas)
#     altura_min=min(alturas)
#     altura_prom=sum(alturas)/len(alturas)
#     print(f'\nParque {parque}')
#     print(f'La altura máxima de {especie} es {altura_max}')
#     print(f'La altura mínima de {especie} es {altura_min}')
#     print(f'La altura promedio de {especie} es {round(altura_prom,2)}')
    
# #Probar función obtener_inclinaciones
# parque='CENTENARIO'
# lista_arboles=leer_parque(nombre_archivo, parque)   
# especie='Falso Guayabo'     
# inclinaciones=obtener_inclinaciones(lista_arboles, especie)

# #Probar función especimen_mas_inclinado
# parque='CENTENARIO'
# lista_arboles=leer_parque(nombre_archivo, parque)
# mas_inclinado=especimen_mas_inclinado(lista_arboles)
# print(mas_inclinado)


# #Probar función especie_promedio_mas_inclinada
# parque='ANDES, LOS'
# lista_arboles=leer_parque(nombre_archivo, parque)
# promedio_mas_inclinada=especie_promedio_mas_inclinada(lista_arboles)
# print(promedio_mas_inclinada)

#%%Ejercicios Clase 04

# import os

# #Si se ejecuta desde un directorio ../ejercicios_python/Clase0x
# #y Data en ejercicios_python

# mycwd=os.getcwd()    #directorio en el cual estoy
# os.chdir('..')       #ir al anterior
# path=os.getcwd()     #obtener path

# arbolado_path='Data/arbolado-en-espacios-verdes.csv'
# nombre_archivo=os.path.join(path, arbolado_path)
# os.chdir(mycwd)


# #Ejercicio 4.16: Lista de alturas del Jacarandá
# arboleda=leer_arboles(nombre_archivo)
# H_jacaranda=[arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com']=='Jacarandá']


# #Ejercicio 4.17: Lista de tuplas (altura, diametro) del jacarandá
# HD_jacaranda=[(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']


# #Ejercicio 4.18: Probar función medidas_de_especies
# especies=['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
# arboleda=leer_arboles(nombre_archivo)
# HD_especies=medidas_de_especies(especies, arboleda)

#%% Clase 05 Ejercicio 5.24: Histograma de altos de Jacarandás

nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
especie = 'Jacarandá'


#graficar_histograma_alturas(nombre_archivo, especie)
graficar_histograma_alturas(arboleda, especie)

#%% Clase 05 Ejercicio 5.25: 
import numpy as np
import os
import matplotlib.pyplot as plt

nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
HD_jacaranda = [(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
h = np.array([h for h, d in HD_jacaranda])
d = np.array([d for h, d in HD_jacaranda])
plt.figure()
plt.scatter(d, h, alpha=0.2, s=10)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")

#%% Clase 5: Ejercicio 5.26:Scatterplot para diferentes especies
import os

nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
#medidas = medidas_de_especies(especies, arboleda)

#Graficos separados
graficar_especies_alt_diam(arboleda,especies, False)
plt.figure()

#Gráficos juntos
graficar_especies_alt_diam(nombre_archivo,especies)
  