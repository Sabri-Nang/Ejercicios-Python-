import csv
import sys

def costo_camion(nombre_archivo):
    'Devuelve el costo total del camion del archivo ingresado'
    with open(nombre_archivo,'rt') as f:
        rows=csv.reader(f)
        headers=next(rows)
        costo_total=0
       
        for row in rows:
            try:
                
                cajones=int(row[1])
                precio=float(row[2])
                costo_total+=cajones*precio
            except:
                print(f'Warning: datos perdidos en la linea {row}')
            
    return costo_total
    
if len(sys.argv)==2:
    nombre_archivo=sys.argv[1]
else:
    nombre_archivo='../Data/camion.csv'
costo=costo_camion(nombre_archivo)
print('Costo total:', costo)
    