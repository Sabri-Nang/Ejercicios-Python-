import csv
import fileparse

def leer_camion(nombre_archivo):
    '''Dado un archivo devuelve el contenido del camion en una lista de diccionarios'''
    camion = fileparse.parse_csv(nombre_archivo, types = [str, int, float])
    return camion


def leer_precios(nombre_archivo):
    '''Recibe un archivo csv y devuelve un diccionario con el nombre del producto
    como clave y el precio como valor
    '''
    precios = fileparse.parse_csv(nombre_archivo, types = [str,float], has_headers = False)
    
    return dict(precios)

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

def imprimir_informe(informe: list):
    '''Recibe una lista de tuplas del tipo (nombre, cajones, precio, cambio)
    e imprime una tabla conteniendo esos datos.
    '''
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')            
    print('%10s %10s %10s %10s' %headers)
    sep=' '
    print(f'{sep:-<10s} {sep:-<10s} {sep:-<10s} {sep:-<10s}')
    for nombre, cajones, precio, cambio in informe:
        precio='$%0.2f'%precio
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')  

def informe_camion(archivo_camion, archivo_precios):
    '''Recibe un archivo con los datos del camión y un archivo con los datos de
    precios e imprime un informe
    '''
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)
    
#%%
#Pruebas  
            
#informe_camion('../Data/camion.csv', '../Data/precios.csv')  
#informe_camion('../Data/camion2.csv', '../Data/precios.csv')    

#files = ['../Data/camion.csv', '../Data/camion2.csv']
#for name in files:
#        print(f'{name:-^43s}')
#        informe_camion(name, '../Data/precios.csv')
#        print() 



    