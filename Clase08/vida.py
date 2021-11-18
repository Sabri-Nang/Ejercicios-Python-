# -*- coding: utf-8 -*-
"""
Created on Sun May  9 02:45:06 2021

@author: Sabri
"""

#segundos vividos

from datetime import datetime

def segundos_vividos(date):
    '''Recibe una cadena de tipo: dia/mes/año.
    Devuelve la cantidad de segundos vividos hasta la actualidad'''
    date_object = datetime.strptime(date, '%d/%m/%Y')
    now = datetime.now()
    delta_time = now - date_object
    print(f'Haz vivido {delta_time.total_seconds()} segundos')
    return delta_time.total_seconds()
    