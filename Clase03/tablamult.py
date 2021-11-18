# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 02:50:11 2021

@author: Sabri
"""
def tabla(n):
    a=range(n+1)   #rango del 0 al 9
    for i in a:
        if i==0:
            headers=f'{i:7d}'
        else:
            headers+=f'{i:5d}' #encabezado, número a multiplicar
    print(headers)
    sep=''
    print(f'{sep:-<53s}')     #línea punteada de separacion
    for i in a:               #recorro del 0 al 9, el i corresponde a la tabla que veo
        line=f'{i:<d}:'       #creo una línea con el número a multiplicar por el 
        ##print()
        ##print(line, end='')
                              #número del encabezado
        num=0                 #primer valor de la tabla    
        for k in a: #for para recorrer todos los valores de la tabla del 0 al 9
            ##print(f'{num:>5d}', end='')
            line+=f'{num:5d}' #agrego el múltiplo a la línea
            num+=i            #al valor anterior, le sumo el valor por el cual
                              #estoy multiplicando (el i)
        print(line)
        
## con la modificación de lo visto en clase
tabla(9)
      
        
    