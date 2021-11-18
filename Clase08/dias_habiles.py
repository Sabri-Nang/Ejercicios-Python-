# -*- coding: utf-8 -*-
"""
Created on Sun May  9 03:28:39 2021

@author: Sabri
"""

#dias_habiles
from datetime import datetime, timedelta

def dias_habiles(inicio, fin, feriados = []):
    '''Recibe inicio y fin del tipo string del tipo dia/mes/año
    y una lista de feriados. Por omisión la lista está vacía
    Devuelve la cantidad de dias hábiles entre esas fechas.
    '''
    inicio = datetime.strptime(inicio, '%d/%m/%Y')
    fin = datetime.strptime(fin, '%d/%m/%Y')
    delta_dias = fin - inicio 
    dias_totales = delta_dias.days + 1  #sumo uno para incluir el ultimo dia
    dias_habiles = dias_totales         
    print(dias_totales)
    for i in range(0, dias_totales):  #recorro todos los dias desde el inicio al fin
        dia = inicio + timedelta(days = i)
        dia_str = dia.strftime('%d/%m/%Y')  #paso el dia en datetime a string
        
        if dia.isocalendar()[2] in [6, 7]:  #si es sábado o domingo lo saco del acumulador
            dias_habiles -= 1
            #print(dia_str, 'es sabado o domingo')
            
        elif dia_str in feriados:     #si es feriado lo saco del acumulador
            dias_habiles -= 1
            #print(dia_str, 'es feriado')
            
    return dias_habiles
    
feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']
dias_habiles = dias_habiles('20/9/2020', '10/10/2020', feriados)
print(dias_habiles)