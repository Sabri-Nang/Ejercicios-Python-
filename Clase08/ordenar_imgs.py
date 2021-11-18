# -*- coding: utf-8 -*-
"""
Created on Sun May  9 07:47:42 2021

@author: Sabri
"""

import os
import datetime
#import time
import shutil

#crear un nuevo directorio en ../Data/img_procesadas

def encontrar_png(directorio):
    '''Recibe un directorio e imprime en pantalla los nombres de todos los 
    archivos .png en el directorio o los subdirectorios'''
    archivos = []
    nombres =[]
    ruta_nombre = []
    #lista_archivos = []
    for root, dirs, files in os.walk(directorio):
        
        for name in files:
            if '.png' in name:
                datos = {}
                #print(os.path.join(root, name))
                archivo = os.path.join(root, name)
                archivos.append(archivo)
                nombres.append(name)
                datos['nombre_archivo'] = name
                datos['ruta_archivo'] = archivo
                ruta_nombre.append(datos)
    return archivos, nombres, ruta_nombre

def setear_modificacion(archivos):
    '''Recibe una lista de archivos y modifica la fecha de acceso y
    modificación según los dígitos del nombre del archivo'''
    for archivo in archivos:
        year = int(archivo[-12:-8])
        month = int(archivo[-8:-6])
        day = int(archivo[-6:-4])
        #stats_archivo = os.stat(archivo)
        fecha_acceso = datetime.datetime(year = year, month = month, day = day)
        fecha_modifi = datetime.datetime(year = year, month = month, day = day)
        ts_acceso = fecha_acceso.timestamp()
        ts_modifi = fecha_modifi.timestamp()
        os.utime(archivo, (ts_acceso, ts_modifi))

def mover(ruta_nombre):
    '''Recibe una lista de diccionarios del tipo {ruta: , nombre: }
    Mueve los archivos de los directorios al directorio ../Data/imgs_procesadas
    '''
    try:
        shutil.rmtree(os.path.join('..', 'Data', 'imgs_procesadas')) #borro la carpeta si ya existe
    except:
        pass
    destino = os.path.join('..', 'Data', 'imgs_procesadas')
    os.mkdir(destino)
    
    for archivo in ruta_nombre:
        #print(destino)
        #print(archivo['nombre_archivo'])
        destino_archivo = os.path.join(destino, str(archivo['nombre_archivo']))
        #print(destino_archivo)
        #print(destino)
        shutil.move(archivo['ruta_archivo'], destino_archivo)
    # for archivo in archivo:
    #     os.rename(archivo, '')
        
def borrar_vacios(directorio):
    '''Borra los subdirectorios vacíos de directorio
    '''
    for root, dirs, files in os.walk(directorio):
        print(root)
        try:  
            os.rmdir(root)
            print(root)
        except:
            pass
        # for name in dirs:
        #     try:
        #         os.rmdir(root)
        #     except:
        #         pass
            
            
directorio = os.path.join('..', 'Data', 'ordenar')
archivos, nombres, ruta_nombre = encontrar_png(directorio)
setear_modificacion(archivos)
mover(ruta_nombre)
borrar_vacios(directorio)

# camino = '../Clase01/rebotes.py'

# stats_archivo = os.stat(camino)
# print(time.ctime(stats_archivo.st_atime))

# fecha_acceso = datetime.datetime(year = 2017, month = 9, day = 21, hour = 19, minute = 51)
# fecha_modifi = datetime.datetime(year = 2012, month = 9, day = 24, hour = 12, minute = 9, second = 24)

# ts_acceso = fecha_acceso.timestamp()
# ts_modifi = fecha_modifi.timestamp()
# os.utime(camino, (ts_acceso, ts_modifi))

# stats_archivo = os.stat(camino)
# print(time.ctime(stats_archivo.st_atime))