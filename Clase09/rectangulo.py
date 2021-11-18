# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:26:11 2021

@author: Sabri
"""

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    
    def __add__(self, b):
        return Punto(self.x + b.x, self.y + b.y)
    
class Rectangulo:
    def __init__(self, p1, p2):
        '''Recibe dos puntos correspondiente a esquinas opuestas
        '''
        self.p1 = p1
        self.p2 = p2
        
    def base(self):
        '''Calcula la base del rectángulo
        '''
        base = abs(self.p1.x - self.p2.x)
        return base
    
    def altura(self):
        '''Calcula la altura del rectángulo
        '''
        altura = abs(self.p1.y - self.p2.y)
        return altura
    
    def area(self):
        '''Devuelve el área del rectángulo
        '''
        area = self.altura() * self.base()
        return area
    
    def __str__(self):
        return f'({self.p1.x}, {self.p1.y})({self.p2.x}, {self.p2.y})({self.p1.x}, {self.p2.y})({self.p2.x}, {self.p1.y})'
    
    def __repr__(self):
        return f'Rectangulo(Punto({self.p1.x}, {self.p1.y}), Punto({self.p2.x}, {self.p2.y}))'
    
    def desplazar(self, punto):
        self.p1 = self.p1 + punto
        self.p2 = self.p2 + punto
        
    def rotar(self):
        '''Rota el rectángulo sobre su esquina inferior derecha 90 grados a la
        derecha'''
        altura = self.altura()
        base = self.base()
        
        if (self.p2.y > self.p1.y):
            
            if (self.p2.x > self.p1.x):
                e_inf_der = Punto(self.p2.x, self.p1.y)
                
            else:
                e_inf_der = self.p1
        
        else:
            if (self.p2.x > self.p1.x):
                e_inf_der = self.p2
            else:
                e_inf_der = Punto(self.p1.x, self.p2.y)
        
        self.p1 = e_inf_der   #Redefino a p1 como el punto del extremo inferior
                              #derecho
        e_sup = Punto(e_inf_der.x + altura, e_inf_der.y + base) #el punto opuesto
                                             #al nuevo p1 luego de la rotación
        self.p2 = e_sup   #redefino a p2 como e_sup
        #print(f'El punto p1 es {self.p1}')
        #print(f'El punto p2 es {self.p2}')
        
#%%
ul = Punto(0, 2)
lr = Punto(1, 0)
ll = Punto(0, 0)
ur = Punto(1, 2)

rect1 = Rectangulo(ul, lr)
rect2 = Rectangulo(ll, ur)

rect1.rotar()
rect2.rotar()            
