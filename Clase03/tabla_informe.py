import csv
def leer_camion(nombre_archivo):
    '''Dado un archivo devuelve el contenido del camion en una lista de diccionarios'''
    camion=[]
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        rows=csv.reader(f)
        headers=next(rows)
        for n_row, row in enumerate(rows, start=1):
            record=dict(zip(headers,row))
            lote={}   #cada lote es un diccionario, con claves: nombre, cajones y precio
            try:
                
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
        if fruta in precios: #busco la fruta en la lista de precios
            precio=precios[fruta]
            cajones=s['cajones']
            total_venta+=precio*cajones
    print(f'\nEl total del costo del camion es: {total_camion:0.2f}')
    print(f'El total de la venta del camión es: {total_venta:0.2f}')
    balance=total_venta-total_camion
    if balance>0:
        print(f'La ganancia es: {balance:0.2f}')
    else:
        print(f'La pérdida es: {abs(balance):0.2f}')

def hacer_informe(camion,precios):
    lista=[]
    for s in camion:
        t=()
        fruta=s['nombre']
        if fruta in precios:
            cambio=round(precios[fruta]-s['precio'],2)
            t=(s['nombre'], s['cajones'], s['precio'], cambio)
            lista.append(t)
    return lista
        
camion=leer_camion('../Data/camion.csv')
precios=leer_precios('../Data/precios.csv')
#balance(camion,precios) 

informe=hacer_informe(camion,precios)      
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')            
print('%10s %10s %10s %10s' %headers)
sep=' '
print(f'{sep:-<10s} {sep:-<10s} {sep:-<10s} {sep:-<10s}')
for nombre, cajones, precio, cambio in informe:
        precio='$%0.2f'%precio
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
    