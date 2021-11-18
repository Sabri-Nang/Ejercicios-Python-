# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:40:51 2021

@author: Sabri
"""

#clase Lote

class Lote:
    '''Defino una clase lote, con atributos: nombre (str), 
    cajones (int) y precio (float)'''
    
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self, n_cajones):
        self.cajones = self.cajones - n_cajones
    
    def __repr__(self):
        return f'Lote(\'{self.nombre}\', {self.cajones}, {self.precio})'      