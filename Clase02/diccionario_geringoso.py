#diccionario_geringoso

def geringoso(lista):
    '''Ingresa una lista y devuelve un diccionario con las palabras de la lista 
    como claves y las palabras en geringoso como valor'''
    d={}    #creo un diccionario vacio
    for palabra in lista:   #recorro la lista de palabras
        papalapabrapa=''    #variable que guarda la palabra en geringoso
        for c in palabra: 
            papalapabrapa=papalapabrapa+c
            if c in 'aeiouAEIOU':
                papalapabrapa=papalapabrapa+'p'+c.lower()
        print(papalapabrapa)
        d[palabra]=papalapabrapa
    return d