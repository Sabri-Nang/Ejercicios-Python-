# -*- coding: utf-8 -*-
"""
Created on Mon May 24 04:37:53 2021

@author: Sabri
"""

#ticker.py

from vigilante import vigilar
import csv
from formato_tabla import crear_formateador
from informe import leer_camion


def cambiar_tipo(rows, types):
    '''Recibe filas y una lista de types
    y convierte los datos de la fila a los tipos de
    detos ingresados
    '''
    for row in rows:
        #(func(val) for func, val in zip(types, row))
        yield [func(val) for func, val in zip(types, row)]
     
def hace_dicts(rows, headers):
    '''Recibe filas y una lista de headers
    Produce un generador de diccionarios con claves los elementos de
    headers y valor los elementos de rows correspondientes
    '''
    for row in rows:
        yield dict(zip(headers, row))
    
        
def parsear_datos(lines):
    rows = csv.reader(lines)
    
    #rows = elegir_columnas(rows, [0, 1, 2])
    #Reemplazo elegir_columnas por la expresión generadora
    rows = ((row[index] for index in [0, 1, 2]) for row in rows) #expresion generadora
    
    #rows = cambiar_tipo(rows, [str, float, int])
    #Reemplazo cambiar_tipos por la expresión generadora
    rows = ((func(val) for func, val in zip([str, float, int], row)) for row in rows)
    
    #rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    #Reemplazo hace_dicts por la expresión generadora
    rows = (dict(zip(['nombre', 'precio', 'volumen'], row)) for row in rows)
    
    return rows

def elegir_columnas(rows, indices):
    '''Generador.
    Dadas filas e índices (lista) produce un generador
    que devuelve una lista con los elementos de la fila
    correspondientes a los índices.
    
    '''
    for row in rows:
        yield [row[index] for index in indices]

def filtrar_datos(filas, nombres):
    '''Recibe filas y nombres.
    Produce un generador filtrando de las filas
    los nombres. 
    '''
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila
    
    
def ticker(camion_file, log_file, fmt):
    '''Recibe un archivo camion, un archivo log
    y un tipo de formateador.
    Crea un undicador en tiempo real en el formateador
    indicado.
    '''
    formateador = crear_formateador(fmt)
    camion = leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file))
    #filas = filtrar_datos(filas, camion)
    #Reemplazo filtrar_datos por la expresión geeradora
    filas = (fila for fila in filas if fila['nombre'] in camion)
    
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
   
    for f in filas:
        rowdata = []
        rowdata = [str(f[clave]) for clave in f]
        formateador.fila(rowdata)


if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)
        
        