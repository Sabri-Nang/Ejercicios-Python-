# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:09:01 2021

@author: Sabri
"""

#fileparse.py
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede indicar si tiene o no encabezados: has_headers. En caso de no indicarlo
    #el parámetro por omisión es True
    '''
    with open(nombre_archivo, encoding='utf-8') as f:
        filas = csv.reader(f)
        registros = []
        
        #Me fijo si tiene o no encabezados    
        if has_headers:    
            encabezados = next(filas)
            #Selecciono cuales serán los encabezados en base a si select es True o False
            if select:
                #si además de encabezados tiene select
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]    
                encabezados = select
            else:
                #si tiene encabezados pero no select
                indices = []
        else:
            #si no tiene encabezados, indices es una lista vacía
            indices = []
        
        
        for fila in filas:
            if not fila:    #Saltea filas sin datos
                continue
            
            #Determino la fila según la lista de índices anterior
            #Si no tiene encabezados la lista de índices es vacía por ende no
            #entra al if siguente y la fila es la original.
            #Si tiene encabezados puedo tener todos o índices o los determinados
            #según el select
            if indices:
                fila = [fila[index] for index in indices]
            
            #Si se indicó types, pasar cada valor de la fila al tipo indicado
            if types:
                fila = [func(val) for func, val in zip(types,fila)]
            
            
            if has_headers:
                #Arma el diccionario en caso de tener encabezados y lo agrega a la 
                #lista de salida
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            else:
                #Arma la tupla en caso de no tener encabezados y lo agrega a lista
                #de salida
                registro = tuple(fila)
                registros.append(registro)     
                
    return registros

#camion = parse_csv('../Data/camion.csv', select=['nombre', 'precio'], types=[str,float])
#precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)
