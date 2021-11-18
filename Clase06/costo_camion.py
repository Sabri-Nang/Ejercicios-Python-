from informe_funciones import leer_camion


def costo_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    costo_total=0.0
    camion = leer_camion(nombre_archivo)
    for registro in camion:
        costo_total+=registro['cajones']*registro['precio']
           
    return costo_total

costo = costo_camion('../Data/fecha_camion.csv')
