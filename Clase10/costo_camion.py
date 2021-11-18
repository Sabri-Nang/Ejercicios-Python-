# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:48:25 2021

@author: Sabri
"""




import informe


def costo_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    
    camion = informe.leer_camion(nombre_archivo)
    
    return camion.precio_total()

def main(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion')
    nombre_archivo = parametros[1]
    costo=costo_camion(nombre_archivo)
    print('Costo total:', costo)
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
    

#costo_camion('../Data/camion.csv')
