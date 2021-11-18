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
                lote={}   #cada lote es un diccionario, con claves: nombre, cajones y precio
                lote['nombre']=record['nombre']
                lote['cajones']=int(record['cajones'])
                lote['precio']=float(record['precio'])
                camion.append(lote)
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
os.chdir('..')
path=os.getcwd()

camion_path='Data\camion.csv'
precios_path='Data\precios.csv'
camion_archivo=os.path.join(path, camion_path)
precios_archivo=os.path.join(path, precios_path)

os.chdir(mycwd)



camion=leer_camion(camion_archivo)
precios=leer_precios(precios_archivo)
balance(camion,precios)
