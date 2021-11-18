# -*- coding: utf-8 -*-
"""
Created on Sun May  9 03:14:28 2021

@author: Sabri
"""

#fecha de reincorporación. Tenés una licencia por xaternidad
#que empieza el 26 de septiembre de 2020 y dura 200 días.
#cuándo te reincorporás

from datetime import datetime, timedelta


inicio_licencia = datetime(2020, 9, 26)
dias_licencia = timedelta(days = 200)

reincorporacion = inicio_licencia + dias_licencia
reincorporacion_str = reincorporacion.strftime('%d/%m/%Y')
print(f'Debes reincorporarte el {reincorporacion_str}')

def reincorporacion(inicio, dias):
    '''Recibe un string del tipo dia/mes/año y la cantidad
    de dias de licencia.
    Devuelve la fecha de reincorporación'''
    inicio_date = datetime.strptime(inicio, '%d/%m/%Y')
    dias = timedelta(days = dias)
    reincorporacion = inicio_date + dias
    reincorporacion_str = reincorporacion.strftime('%d/%m/%Y')
    print(f'Debes reincorporarte el {reincorporacion_str}')