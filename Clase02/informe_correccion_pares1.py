# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:09:27 2021

@author: Sabri
"""

#%%Ejercicio 2.16: Lista de diccionarios
from pprint import pprint
import os
#os.chdir(r"C:\Users\Lucho\Desktop\ejercicios_python")
import csv
def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo, 'rt') as f:
        filas=csv.reader(f)
        headers = next(filas)
        for fila in filas:
            try:
                lote ={"nombre":fila[0],
                       "cajones":int(fila[1]),
                       "precio":float(fila[2])
                       }
                camion.append(lote)
            except ValueError:
                print("Warning: Fila sin datos correctos")
        total = 0.0
       #for s in camion:
        #  total += s[1] * s[2]

       # print(total)
    return camion
camion = leer_camion('../Data/camion.csv')
pprint(camion)
#%%Ejercicio 2.17: Diccionarios como contenedores
from pprint import pprint
import os
#os.chdir(r"C:\Users\Lucho\Desktop\ejercicios_python")
import csv
def leer_precios(nombre_archivo):
    precios={}
    with open(nombre_archivo, 'rt') as f:
        filas=csv.reader(f)
        precios={}
        for fila in filas:
            
            try:
                precios[fila[0]] =float(fila[1])   
            except IndexError:
                print("Warning: Fila sin datos correctos")
        total = 0.0
       #for s in camion:
        #  total += s[1] * s[2]

       # print(total)
    return precios
precios = leer_precios('../Data/precios.csv')
pprint(precios)
#%%Ejercicio 2.18: Balances
def balance(camion,precios):
    #costo del camion
    costo_camion=0
    recaudacion=0
    for lote in camion:
        costo_camion+=lote["cajones"]*lote["precio"]
    #Recaudacion de venta
        if lote["nombre"] in precios:
            recaudacion+=precios[lote["nombre"]]*lote["cajones"]
    resultado = recaudacion-costo_camion
    if resultado>0:
        print(f"Se obtuvo una ganancia de ${round(resultado,2)}")
    else:
        print(f"Se obtuvo una perdida de ${round(resultado,2)}")
    return resultado

camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
balance(camion,precios)