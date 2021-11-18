# -*- coding: utf-8 -*-
"""
Created on Tue May 11 07:48:28 2021

@author: Sabri
"""

import os
import pandas as pd

direc1 = '..'
direc2 = 'Data'

a_parques = 'arbolado-en-espacios-verdes.csv'
a_veredas = 'arbolado-publico-lineal-2017-2018.csv'

#determino la ubicación de cada archivo
archivo_parques = os.path.join(direc1, direc2, a_parques)  
archivo_veredas = os.path.join(direc1, direc2, a_veredas)

#creo los dataframes con los datos de cada archivo
df_parques = pd.read_csv(archivo_parques)
df_veredas = pd.read_csv(archivo_veredas)

#creo dataframes para la especie Tipuana tipu seleccionando de los dataframes
#principales la especie y las columnas correspondientes a la altura y el 
#diámetro y creo una copia
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 
                              'Tipuana Tipu'][['altura_tot', 
                                              'diametro']].copy()
            
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 
                              'Tipuana tipu'][['altura_arbol', 
                                              'diametro_altura_pecho']].copy()
                                             
#renombro las columnas para que coincidan
df_tipas_parques.rename(columns = {'altura_tot' : 'altura_arbol',
                                   'diametro' : 'diametro_altura_pecho'}, 
                        inplace = True)
# df_tipas_veredas.rename(columns = {'altura_arbol' : 'altura', 
#                                    'diametro_altura_pecho' : 'diametro'}, 
#                         inplace = True)

#Agrego una columna 'ambiente' con valores 'parque' y 'vereda' según el caso
df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

#Concateno los dataframe de parques y veredas
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

#boxplot para los diámetros
df_tipas.boxplot('diametro_altura_pecho', by = 'ambiente')

#boxplot para las alturas
df_tipas.boxplot('altura_arbol', by = 'ambiente')


#Para otras especies debería cambiar el nombre científico.
#por ejemplo en df_tipas_veredas reemplazar 'Tipuana tipu'
#También se puede crear con una función determinando la especie y el ambiente: 

def df_especie_ambiente(especie, ambiente):
    '''Recibe una especie y un ambiente (str) devuelve un dataframe con las 
    columnas 'altura_arbol', 'diametro_altura_pecho' y 'ambiente' 
    correspondiente a la especie y al ambiente ingresado'''

    direc1 = '..'
    direc2 = 'Data'

    a_parques = 'arbolado-en-espacios-verdes.csv'
    a_veredas = 'arbolado-publico-lineal-2017-2018.csv'
    try:
        if ambiente == 'parque':
            archivo = os.path.join(direc1, direc2, a_parques) #archivo parque
            df = pd.read_csv(archivo)   #genero el df 
            
            #creo un dataframe filtrando la especie ingresada
            #y que contenga solo las columnas altura_tot y diametro
            df_esp_amb = df[df['nombre_cie'] == especie][['altura_tot',
                                                          'diametro']].copy()
            
            #renombro las columnas
            df_esp_amb.rename(columns = {'altura_tot' : 'altura_arbol',
                                   'diametro' : 'diametro_altura_pecho'}, 
                              inplace = True)
            
                                                                            
    
        elif ambiente == 'vereda':
            archivo = os.path.join(direc1, direc2, a_veredas ) #archivo vereda
            df = pd.read_csv(archivo)   #genero el df 
            
            #creo un dataframe filtrando la especie y que contenga solo las 
            #columnas altura_arbol y diametro_altura_pecho
            df_esp_amb = df[df['nombre_cientifico'] == especie][['altura_arbol', 
                                              'diametro_altura_pecho']].copy()
        
        else:    
            return 'No se puede crear el dataframe o no se encuentra el archivo' 
        #si no puedo generar la ubicación del path, termino la ejecución
        
        df_esp_amb['ambiente'] = ambiente   #genero una columna ambiente
        
        return df_esp_amb
    except:
        return 'No se puede leer el archivo'

      
    










