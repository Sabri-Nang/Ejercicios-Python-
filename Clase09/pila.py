# -*- coding: utf-8 -*-
"""
Created on Wed May 19 00:02:11 2021

@author: Sabri
"""

class Pila:
    def __init__(self):
        self.estados = []
    
    def apilar(self, estado):
        self.estados.append(estado)
    
    def desapilar(self):
        return self.estados.pop()
    
    def esta_vacia(self):
        return len(self.estados) == 0
#%%
def mostrar_x_del_estado(estado):
    print(f"Ejecutando {estado['funcion']}(), x vale {estado['variables']['x']}")
    

#%%
pila_de_llamadas = Pila()
estado = {'funcion': 'g', 'proxima_linea_a_ejecutar': 3, 'variables': {'x': 10, 'b': 45}}
mostrar_x_del_estado(estado)
estado['proxima_linea_a_ejecutar'] = 5
pila_de_llamadas.apilar(estado)
estado = {'funcion': 'f', 'proxima_linea_a_ejecutar': 3, 'variables': {'x': 50, 'a': 20}}
mostrar_x_del_estado(estado)
estado = pila_de_llamadas.desapilar()
mostrar_x_del_estado(estado)