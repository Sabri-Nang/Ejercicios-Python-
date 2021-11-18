#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de tipo semántico. Se debía a que al realizar la primer
#combrobación ya retornaba un True o un False y no se ejecutaba todo el bucle while
#    Lo corregí sacando el else que devolvía el False dentro del while y agregué
#un return False cuando sale del ciclo while. También pasé a minúcula la letra que
#toma. En caso de que no encuentre una a devuelve lo que esta en el return final, 
#si encuentra una 'a' al entrar al if, devuelve True
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0    
    while i<n:
        if expresion[i].lower() == 'a': 
            return True
        i += 1
    return False
        
tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de sintaxis. Estaba ubicado luego del if donde había
#un '=' en lugar de '=='. Luego de def, while e if faltan los ':' 
#Está escrito Falso en lugar de False
#Lo corregí agregando un '=' en if expresion[i]='a' y los ':' en def tiene_a(expresion):
#while i<n: y if expresion[i]=='a':
#Y cambiando Falso por False.
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: Tiene un error en tiempo de ejecución. Se soluciona pasando
#a string la variable expresion
#    A continuación va el código corregido

def tiene_uno(expresion):
    expresion=str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%%
#Ejercicio 3.4. Función suma()
#Comentario: Tiene un error semántico, se ejecuta pero no da lo que debería dar.
#Falta el return c.
#Lo corregí agregando la instrucción return c
#    A continuación va el código corregido

def suma(a,b):
    c=a+b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.5:Pisando la memoria.
#Comentario: Tiene un error semántico, registro {} estaba definido fuera del for
#Cada vez que entra al for cambia los valores del diccionario registro y a su vez
#agrega de nuevo el diccionario a camion.
#    A continuación va el código corregido
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    
    with open(nombre_archivo, "rt") as f:
        filas=csv.reader(f)
        encabezado=next(filas)
        
        for fila in filas:
            registro={}
            registro[encabezado[0]]=fila[0]
            
            registro[encabezado[1]]=int(fila[1])
            registro[encabezado[2]]=float(fila[2])
            #print(registro)
            camion.append(registro)
            
    return camion
camion=leer_camion("../Data/camion.csv")
pprint(camion)
