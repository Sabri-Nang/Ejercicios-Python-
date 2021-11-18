def sumcount(n):
    '''
    Devuelve la suma de los primeros n enteros
    '''
    total=0
    while n>0:
        total+=n
        n-=1
    return total