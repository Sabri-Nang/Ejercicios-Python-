# -*- coding: utf-8 -*-
"""
Created on Tue May 18 19:39:00 2021

@author: Sabri
"""
#canguro_bueno.py

class Canguro:
    '''Un canguro es un marsupial
    '''
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenido_marsupio = []
        
    def __str__(self):
        
        if len(self.contenido_marsupio) != 0:
            t = [ self.nombre + ' tiene en su marsupio: ' ]
            for contenido in self.contenido_marsupio:
                s = '    ' + object.__str__(contenido)
                t.append(s)
            return '\n'.join(t)
        else:
            return f'{self.nombre} no tiene contenido en su marsupio'
    
    def meter_en_marsupio(self, item):
        '''Agrega un nuevo item al marsupio
        '''
        
        self.contenido_marsupio.append(item)
        
#%%
#canguro_malo.py
import copy
 
class Canguro:
    '''Un canguro es un marsupial
    '''
    def __init__(self, nombre, contenido = None):
        #cuando ejecuta la clase siempre pasa una sola vez por la def del init
        #y luego entra a los atributos. Una vez q entro en otra instancia
        #no vuelve a hacer contenido=[], porq esta en el parametro q 
        #se paso
        #si defino el parametro por defecto como lista vacia luego se
        #pisan. Porque al leer las clases, sin llamarlas, carga primero
        #los def__init__(...), __str__(...)
        #pongo contenido como None y dentro determino si es vacia o no
        
        #cuando el parametro por defecto no esta definido es mas prolijo 
        #usar None
        '''Inicializar los contenidos del marsupio
        
        nombre: string
        contenido: contenido inicial del marsupio, lista.
        '''
        if not contenido:
            contenido = []
        self.nombre = nombre
        self.contenido_marsupio = contenido
       
        
    def __str__(self):
        '''Devuelve una representación como cadena
        de este Canguro
        '''
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)
    
    def meter_en_marsupio(self, item):
        '''Agrega un nuevo item al marsupio
        '''
        self.contenido_marsupio.append(item)
        
        
        
#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)
print(cangurito)
        
        