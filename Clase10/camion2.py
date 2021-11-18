# -*- coding: utf-8 -*-

class Camion:
    def __init__(self,lotes):
        self.lotes = lotes
        
    def __iter__(self):
        """Vuelve iterable a los objetos de mi clase clase"""
        return self.lotes.__iter__()
    
    def __len__(self):
        """Devuelve la cantidad de lotes de fruta que tiene mi camión"""
        return len(self.lotes)
    
    def __getitem__(self,index):
        """Devuelve el resultado a partir de un índice"""
        return self.lotes[index]
    
    def __contains__(self, nombre):
        """Verifica si una fruta se encuentra en mi lote"""
        return any(lote.nombre == nombre for lote in self.lotes)
    
    def __delitem__(self,index):
        """Remueve un ítem a partir de un indice """
        del self.lotes[index]
        return f'{index} borrado'
    
    def precio_total(self):
        return sum(l.costo() for l in self.lotes)
    
    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
            
        return cantidad_total