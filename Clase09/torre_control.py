# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:35:14 2021

@author: Sabri
"""

class Cola:
    '''Representa a una cola, con operaciones de encolar y
    desencolar. 
    El primero en ser encolado es tambien el primero en ser 
    desencolado
    '''
    
    def __init__(self):
        '''Crea una cola vacía.'''
        self.items = []
        
    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)
    
    def desencolar(self):
        '''Elimina el primer elemento de la cola
        y devuelve su valor.
        Si la cola esta vacía, levanta ValueError.
        '''
        if self.esta_vacia():
            raise ValueError('La cola está vacía')
        return self.items.pop(0)
    
    def esta_vacia(self):
        '''Devuelve 
        True si la cola está vacía,
        False si no.'''
        return len(self.items) == 0
    


class TorreDeControl:
    '''Clase define una torre de control de un aeropuerto.
    Atributos arribos y despegues instancias de la clase Cola.
    
    '''
    def __init__(self):
        '''Inicializo el contenido de la torre.
        
        arribos: instacia de la clase Cola
        despegues: instancia e la clase Cola
        '''
        self.arribos = Cola()
        self.despegues = Cola()
        
    def nuevo_arribo(self, x):
        '''Agrega el vuelo a arribos
        '''
        self.arribos.encolar(x)
    
    def nueva_partida(self, x):
        '''Agrega el vuelo a despegues
        '''
        self.despegues.encolar(x)
        
    def ver_estado(self):
        '''Muestra los vuelos esperanndo aterrizar o despegar.
        '''
        if len(self.arribos.items) != 0:
        
            s = ['Vuelos esperando para aterrizar: ']
            for obj in self.arribos.items:
                t = ' ' + object.__str__(obj)
                s.append(t)
            print(''.join(s))
        else:
            print('No hay vuelos esperando para aterrizar')
        
        if len(self.despegues.items) != 0:
            s = ['Vuelos esperando para despegar: ']
            for obj in self.despegues.items:
                t = ' ' + object.__str__(obj)
                s.append(t)
            print(''.join(s))
        else:
            print('No hay vuelos esperando para despegar')
        
    def asignar_pista(self):
        '''Muestra un mensaje indicando el si el vuelo aterrizó o despegó.
        Tienen prioridad los vuelos que esperan aterrizar.
        Una vez que todos aterrizaron, paso a los vuelos por despegar.
        En caso de no haber vuelos por aterrizar ni despegar indicará
        que no hay vuelos en espera.            
        '''
        if (len(self.arribos.items) != 0):   #Si hay vuelos esperando aterrizar
                                             #tienen prioridad
            aterrizar = self.arribos.desencolar()           
            print(f'El vuelo {aterrizar} aterrizó con éxito')
        
        elif (len(self.despegues.items) != 0):  #Si no hay vuelos para aterrizar
                                                #paso a los vuelos por despegar
            despegar = self.despegues.desencolar()
            print(f'El vuelo {despegar} despegó con éxito')
        
        else:
            print('No hay vuelos en espera')
            
        
        
            
        
       
#%%
torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()   
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()        
        