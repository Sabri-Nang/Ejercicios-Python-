# -*- coding: utf-8 -*-
"""
Created on Sun May  9 05:45:59 2021

@author: Sabri
"""

import os

#devolver el directorio actual
#os.getcwd() get current working directory
directorio_actual = os.getcwd()
print(directorio_actual)


#cambiar directorio de trabajo
#'.' es el actual
#'..' es el directorio anterior
#'/' es el directorio raiz

os.chdir('../Data')
print(os.getcwd())
os.chdir('..')
os.chdir('..')
print(os.getcwd())

#independientemente del sistema operativo
directorio = os.path.join('C:\\','Users','Sa', 'Documents', 'Python UNSAM', 'ejercicios_python', 'Clase08')
os.chdir(directorio)

#listar directorios y archivos
os.getcwd()
os.listdir('../Data')

#Crear un nuevo directorio con mkdir()
# os.mkdir('test')  #creo el directorio llamado test
# os.mkdir(os.path.join('test', 'carpeta'))  #creo subdirectorio carpeta
# os.listdir('test')

#renombrar un directorio, rename(nombre_viejo, nombre_nuevo)
#os.chdir('test')   #entro a test
#os.listdir()     #listo lo que contiene test
#os.rename('carpeta', 'carpeta_nueva')   #renombro a carpeta como carpeta_nueva
#os.listdir()

os.chdir('..')
os.listdir('test')

#se puede renombrar de la siguiente forma
os.rename(os.path.join('test', 'carpeta_nueva'), os.path.join('test', 'carpeta_vieja'))

#si quiero mover el directorio
os.rename(os.path.join('test', 'carpeta_vieja'), 'carpeta_vieja')
os.listdir('test')
#rename funciona cuando no cambio de particion, para eso uso el modulo shutil

#eliminar un archivo
#os.remove('archivo.txt')

#eliminar un directorio
#os.rmdir('directorio')

#para eliminar un directorio no vacio usar rmtree() del modulo shutil

#crear una carpeta dentro de test
os.mkdir(os.path.join('test', 'carpeta'))
os.mkdir(os.path.join('test', 'carpeta', 'subcarpeta'))
os.rmdir('carpeta') #salta error porq no esta vacia

#para eliminar un directorio no vacio
import shutil

#shutil.rmtree('carpeta')


#la funcion walk() del modulo os genera una lista
#con los nombres de todos los archivo de los subdirectorios de un 
#directorio dado
for root, dirs, files in os.walk('.'):
    for name in files:
       print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
        

