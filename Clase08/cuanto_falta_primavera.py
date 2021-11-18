# -*- coding: utf-8 -*-
"""
Created on Sun May  9 03:01:17 2021

@author: Sabri
"""

#cuanto falta para la primavera
from datetime import datetime

def cuanto_falta_primavera():
    hoy = datetime.now()
    primavera = datetime(2021, 9, 21)
    falta = primavera - hoy
    print('Suena musica de Crónica...')
    print(f'Faltan {falta.days} para la primavera!!!')
    
cuanto_falta_primavera()