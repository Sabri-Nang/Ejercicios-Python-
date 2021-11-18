import csv
def leer_precios(nombre_archivo):
    precios={} #diccionario vacío donde irán las claves (nombre de fruta) y su precio como valor
    with open(nombre_archivo, 'rt') as f:
        rows=csv.reader(f)
        
        for row in rows:   #recorrer por líneas
            try:
                nombre=row[0]
                precio=float(row[1])
                precios[nombre]=precio   #nombre como clave, precio como valor
            except:  #si hay líneas vacías que las salteé
                pass
    return precios