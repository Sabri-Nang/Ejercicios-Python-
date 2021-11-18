# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:09:01 2021

@author: Sabri
"""

#fileparse.py
import csv

def parse_csv(lines, select = None, types = None, has_headers=True, silence_error = False):
    '''
    Parsea un archivo en una lista de registros
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede indicar si tiene o no encabezados: has_headers. En caso de no indicarlo el parámetro por omisión es True
    silence_error por omisión False. Silencia errores en el parseo.
    '''
    #with open(nombre_archivo, encoding='utf-8') as f:
    #filas = read_data(lines)
    filas = csv.reader(lines)
      
    #filas = csv.reader(f)
    registros = []
    
    #Lanzo una excepción
    if not has_headers and select:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
        
    #Me fijo si tiene o no encabezados 
    try:
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
        
        
        for i, fila in enumerate(filas):
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
                try:
                    fila = [func(val) for func, val in zip(types,fila)]
                except ValueError as e:
                    if not silence_error:
                        print(f'Fila {i+1}: No pude convertir {fila}')
                        print(f'Fila {i+1}: Motivo {e}')
                    continue
                
            
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
    except Exception as e:
        print(e)

#%%
# import gzip

# with gzip.open('../Data/camion.csv.gz', 'rt') as file:
#    camion = parse_csv(file, types=[str, int,float])

