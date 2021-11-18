def buscar_precios(fruta):
    'Busca el precio de la fruta ingresada'

    f=open('../Data/precios.csv','rt')
    precio=[]
    for line in f:
        row=line.split(',')
        if row[0]==fruta:
            precio=row[1]
            print(f'El precio del cajón de {fruta} es: {precio}')
            break
        
    if precio==[]:
        print(f'{fruta} no figura en el listado de precios')
        

    f.close()
 