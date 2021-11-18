#Leer archivos comprimidos

#Debo importar gzip

import gzip

with gzip.open('../Data/camion.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')

#Observación: La inclusión del modo 'rt' es crítica acá. Si te lo olvidás, vas a 
#estar leyendo cadenas de bytes en lugar de cadenas de caracteres.