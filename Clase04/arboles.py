# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 17:02:48 2021

@author: Sabri
"""
import csv
from collections import Counter

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
        especie=arbol['nombre_com']
        especies.append(especie)
    especie=set(especies)
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
        
        

#%% Probar funcion lista_arboles

import os

#Si se ejecuta desde un directorio ../ejercicios_python/Clase0x
#y Data en ejercicios_python
mycwd=os.getcwd()    #directorio en el cual estoy
os.chdir('..')
path=os.getcwd()

arbolado_path='Data/arbolado-en-espacios-verdes.csv'
nombre_archivo=os.path.join(path, arbolado_path)
os.chdir(mycwd)



#lista_arboles=leer_parque(nombre_archivo, 'GENERAL PAZ')

#probar función especies
#especs=especies(lista_arboles)

#probar función contar_ejemplares
#ejemplares=contar_ejemplares(lista_arboles)

#probar función especies_mas frecuentes
#parques=['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
#especies_mas_frecuentes('../Data/arbolado-en-espacios-verdes.csv', parques)


#Probar función obtener alturas
#parques=['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
#especie='Jacarandá'  
 
#for parque in parques:
#    alturas=obtener_alturas(leer_parque(nombre_archivo, parque), especie)        
#    altura_max=max(alturas)
#    altura_min=min(alturas)
#    altura_prom=sum(alturas)/len(alturas)
#    print(f'\nParque {parque}')
#    print(f'La altura máxima de {especie} es {altura_max}')
#    print(f'La altura mínima de {especie} es {altura_min}')
#    print(f'La altura promedio de {especie} es {round(altura_prom,2)}')
    
#Probar función obtener_inclinaciones
#parque='CENTENARIO'
#lista_arboles=leer_parque(nombre_archivo, parque)   
#especie='Falso Guayabo'     
#inclinaciones=obtener_inclinaciones(lista_arboles, especie)

#Probar función especimen_mas_inclinado
#parque='CENTENARIO'
#lista_arboles=leer_parque(nombre_archivo, parque)
#mas_inclinado=especimen_mas_inclinado(lista_arboles)
#print(mas_inclinado)


#Probar función especie_promedio_mas_inclinada
#parque='ANDES, LOS'
#lista_arboles=leer_parque(nombre_archivo, parque)
#promedio_mas_inclinada=especie_promedio_mas_inclinada(lista_arboles)
#print(promedio_mas_inclinada)

#%%Ejercicios Clase 04

import os

#Si se ejecuta desde un directorio ../ejercicios_python/Clase0x
#y Data en ejercicios_python

mycwd=os.getcwd()    #directorio en el cual estoy
os.chdir('..')       #ir al anterior
path=os.getcwd()     #obtener path

arbolado_path='Data/arbolado-en-espacios-verdes.csv'
nombre_archivo=os.path.join(path, arbolado_path)
os.chdir(mycwd)


#Ejercicio 4.19: Lista de alturas del Jacarandá
arboleda=leer_arboles(nombre_archivo)
H_jacaranda=[arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com']=='Jacarandá']


#Ejercicio 4.20: Lista de tuplas (altura, diametro) del jacarandá
HD_jacaranda=[(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']


#Ejercicio 4.20: Probar función medidas_de_especies
especies=['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
arboleda=leer_arboles(nombre_archivo)
HD_especies=medidas_de_especies(especies, arboleda)