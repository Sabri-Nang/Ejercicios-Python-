# -*- coding: utf-8 -*-
"""
Created on Sun May  9 07:18:16 2021

@author: Sabri
"""

import os

def encontrar_png(directorio):
    '''Recibe un directorio e imprime en pantalla los nombres de todos los 
    archivos .png en el directorio o los subdirectorios'''

    for root, dirs, files in os.walk(directorio):
        #arc1 = ((directorio, name) for name in files if '.png' in name)
        
        #arc2 = ((directorio, name) for name in dirs if '.png' in name)
        for name in files:
            arc1 = ((directorio, name) for name in files if '.png' in name)
            
        #     if '.png' in name:
        #         print(os.path.join(root, name))
        #for name in dirs:
         #   arc2 = ((directorio, name) for name in dirs if '.png' in name)
        #     if '.png' in name:
        #         print(os.path.join(root, name))
        
        
    
directorio = os.path.join('..', 'Data', 'ordenar')

encontrar_png(directorio)
