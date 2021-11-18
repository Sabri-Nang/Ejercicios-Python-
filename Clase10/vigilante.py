# -*- coding: utf-8 -*-
"""
Created on Mon May 24 03:36:45 2021

@author: Sabri
"""

#vigilante.py

import os
import time


def vigilar(archivo):
    with open(archivo) as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.5)
                continue
            yield line

if __name__ == '__main__':
    import informe
    
    camion = informe.leer_camion('../Data/camion.csv')
    
    for line in vigilar('../Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if volumen > 1000:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
