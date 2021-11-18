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
    
        
        

#%% Probar funcion lista_arboles
nombre_archivo='../Data/arbolado-en-espacios-verdes.csv'
lista_arboles=leer_parque(nombre_archivo, 'GENERAL PAZ')

#probar función especies
especs=especies(lista_arboles)

#probar función contar_ejemplares
ejemplares=contar_ejemplares(lista_arboles)

#probar función especies_mas frecuentes
parques=['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
especies_mas_frecuentes('../Data/arbolado-en-espacios-verdes.csv', parques)


#Probar función obtener alturas
parques=['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
especie='Jacarandá'  
 
for parque in parques:
    alturas=obtener_alturas(leer_parque(nombre_archivo, parque), especie)        

    altura_max=max(alturas)
    altura_min=min(alturas)
    altura_prom=sum(alturas)/len(alturas)
    print(f'\nParque {parque}')
    print(f'La altura máxima de {especie} es {altura_max}')
    print(f'La altura mínima de {especie} es {altura_min}')
    print(f'La altura promedio de {especie} es {round(altura_prom,2)}')
    
#Probar función obtener_inclinaciones
parque='CENTENARIO'
lista_arboles=leer_parque(nombre_archivo, parque)   
especie='Falso Guayabo'     
inclinaciones=obtener_inclinaciones(lista_arboles, especie)

#Probar función especimen_mas_inclinado
nombre_archivo='../Data/arbolado-en-espacios-verdes.csv'
parque='CENTENARIO'
lista_arboles=leer_parque(nombre_archivo, parque)
mas_inclinado=especimen_mas_inclinado(lista_arboles)
print(mas_inclinado)


#Probar función especie_promedio_mas_inclinada
parque='ANDES, LOS'
lista_arboles=leer_parque(nombre_archivo, parque)
promedio_mas_inclinada=especie_promedio_mas_inclinada(lista_arboles)
print(promedio_mas_inclinada)

