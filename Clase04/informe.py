import csv
def leer_camion(nombre_archivo):
    '''Dado un archivo devuelve el contenido del camion en una lista de diccionarios'''
    camion=[]
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        rows=csv.reader(f)
        headers=next(rows)
        for n_row, row in enumerate(rows, start=1):
            record=dict(zip(headers,row))
            try:
                #lote={}   #cada lote es un diccionario, con claves: nombre, cajones y precio
                #lote['nombre']=record['nombre']
                record['cajones']=int(record['cajones'])
                record['precio']=float(record['precio'])
                camion.append(record)
            except ValueError:
                print(f'Fila {n_row}: No pude interpretar: {row}')
    return camion


def leer_precios(nombre_archivo):
    precios={} #diccionario vacío donde irán las claves (nombre de fruta) y su precio como valor
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        rows=csv.reader(f)
        
        for row in rows:   #recorrer por líneas
            try:
                nombre=row[0]
                precio=float(row[1])
                precios[nombre]=precio   #nombre como clave, precio como valor
            except:  #si hay líneas vacías que las salteé
                pass
    return precios


def balance(camion, precios):
    total_camion=0.0 
    total_venta=0.0
    for s in camion:
        total_camion+=s['cajones']*s['precio']      
        fruta=s['nombre']
        #if fruta in precios: #busco la fruta en la lista de precios
        precio=precios[fruta]
           # cajones=s['cajones']
        total_venta+=precio*s['cajones']
    print(f'\nEl total del costo del camion es: {total_camion:0.2f}')
    print(f'El total de la venta del camión es: {total_venta:0.2f}')
    if total_venta-total_camion>0:
        print(f'La ganancia es: {total_venta-total_camion:0.2f}')
    else:
        print(f'La pérdida es: {abs(total_venta-total_camion):0.2f}')

#%%
import os

#Si se ejecuta desde un directorio ../ejercicios_python/Clase0x
#y Data en ejercicios_python
mycwd=os.getcwd()    #directorio en el cual estoy
os.chdir('../Data')  #voy a la carpeta Data
path=os.getcwd()     #Obtengo el path de Data

camion_path='camion.csv'
precios_path='precios.csv'
camion_archivo=os.path.join(path, camion_path)
precios_archivo=os.path.join(path, precios_path)
os.chdir(mycwd)  #vuelvo al directorio del cual partí



camion=leer_camion(camion_archivo)
precios=leer_precios(precios_archivo)
balance(camion,precios)

#costo del camión
costo=sum([s['cajones']*s['precio'] for s in camion])

#valor en el mercado de la carga del camión
valor=sum([s['cajones']*precios[s['nombre']] for s in camion])

#%%
#Consulta de datos

#Todas las frutas que tienen mas de 100 cajones
mas100=[s for s in camion if s['cajones']>100]
mas100

#Información sobre cajones de Mandarina y Naranja
myn=[s for s in camion if s['nombre'] in {'Mandarina', 'Naranja'}]
myn

#Frutas que costaron mas de $10000
costo10k=[s for s in camion if s['cajones']*s['precio']>10000]
costo10k

#%%Extraccion de datos
#construir una lista de tuplas (nombre, cajones) que indique la cantidad
#de cajones de cada fruta tomando los datos de camión

nombre_cajones=[(s['nombre'], s['cajones']) for s in camion]
nombre_cajones

nombres={s['nombre'] for s in camion}
nombres

stock={nombre:0 for nombre in nombres}
stock
for s in camion:
    stock[s['nombre']]+=s['cajones']
stock

camion_precios={nombre:precios[nombre] for nombre in nombres}
camion_precios

#%%Extraer datos de un archivo csv

import csv
f=open('../Data/fecha_camion.csv')
rows=csv.reader(f)
headers=next(rows)
headers
select=['nombre', 'cajones', 'precio']
indices=[headers.index(ncolumna) for ncolumna in select]
indices
row=next(rows)
record={ncolumna: row[index] for ncolumna, index in zip(select,indices)}
record

f=open('../Data/fecha_camion.csv')
rows=csv.reader(f)
headers=next(rows)
select=['nombre', 'cajones', 'precio']
indices=[headers.index(ncolumna) for ncolumna in select]
camion=[{ncolumna:row[index] for ncolumna, index in zip(select,indices)} for row in rows]
camion
