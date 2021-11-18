# -*- coding: utf-8 -*-
"""
Created on Mon May 31 05:17:38 2021

@author: Sabri
"""

def posiciones_de(cadena, subcadena):
    '''Recibe una cadena y devuelve una lista con las posiciones
    de la subcadena dentro de la cadena
    '''
    posiciones = []  #caso base (no esta la subcadena en la cadena), 
                     #no entra en el if y devuelve []
    
    def posicion_aux(cadena, subcadena, posiciones):
        '''Devuelve una lista de con los valores de las posiciones de una
        subcadena en una cadena de forma iterativa.
        Se ejecuta hasta que no encuentra la subcadena en la cadena
        '''
        ncadena = cadena
        
        #print(f'Entro con la cadena: {cadena}')
        if subcadena in ncadena:  
            pos = ncadena.find(subcadena)  #encuentro la posicion  de la 
                                           #primera ocurrencia en la cadena
            
            #una vez que la encontré reemplazo por '*' en cada caracter en 
            #la primer ocurrencia
            ncadena = ncadena.replace(subcadena, '*'*len(subcadena), 1)
            
            posiciones.append(pos)  #agrego la posición a la lista
            #print(f'La lista de posiciones queda {posiciones}')
            
            
            posiciones = posicion_aux(ncadena, subcadena, posiciones)  #vuelvo a 
                                                                  #ejecutar la función
                                                                  #sobre la nueva cadena
                                                                  #Tomando como cadena de 
                                                                  #posiciones lo devuelto en
                                                                  #el paso anterior
        return posiciones
    
    
    if subcadena in cadena:  
        posiciones= posicion_aux(cadena, subcadena, posiciones)
    
    return posiciones

cadena = 'Un tete a tete con Tete'
subcadena = 'te'    
posiciones = posiciones_de(cadena, subcadena)
print(posiciones)

cadena = 'La de la casa estaba en orden porque el casamiento fue casado'
subcadena = 'casa'
posiciones = posiciones_de(cadena, subcadena)
print(posiciones)
