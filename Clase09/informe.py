
# Informe_funciones
 
import fileparse
import lote
import formato_tabla

def leer_camion(nombre_archivo):
    '''Dado un archivo devuelve el contenido del camion en una lista de objetos lote'''
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        camion_dicts = fileparse.parse_csv(f, types = [str, int, float])
    
    camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return camion


def leer_precios(nombre_archivo):
    '''Recibe un archivo csv y devuelve un diccionario con el nombre del producto
    como clave y el precio como valor
    '''
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        precios = fileparse.parse_csv(f, types = [str,float], has_headers = False)
    
    return dict(precios)

def balance(camion, precios):
    total_camion=0.0 
    total_venta=0.0
    for s in camion:
        total_camion+=s.cajones*s.precio     
        fruta=s.nombre
        if fruta in precios: #busco la fruta en la lista de precios
            precio=precios[fruta]
            cajones=s.cajones
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
        fruta=s.nombre
        if fruta in precios:
            cambio=round(precios[fruta]-s.precio,2)
            t=(s.nombre, s.cajones, s.precio, cambio)
            lista.append(t)
    return lista

def imprimir_informe(data_informe, formateador):
    '''Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia)
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])            
    
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)
        
def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    #Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    
    #Crea los datos para el informe
    data_informe = hacer_informe(camion, precios)
    
    formateador = formato_tabla.crear_formateador(fmt)
    
    #Imprimir informe
    imprimir_informe(data_informe, formateador)

def main(parametros):
    if len(parametros) <= 3:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion archivo_precios fmt(opc)')
    archivo_camion = parametros[1]
    archivo_precios = parametros[2]
    if parametros[3]:
        fmt = parametros[3]
        informe_camion(archivo_camion, archivo_precios, fmt)
    else:
        informe_camion(archivo_camion, archivo_precios)
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
    