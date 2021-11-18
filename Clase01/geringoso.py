#geringoso

cadena='Asia'
capadepenapa=''
for c in cadena:
    capadepenapa=capadepenapa+c
    if c in 'aeiouAEIOU':
       capadepenapa=capadepenapa+'p'+c.lower()
print(capadepenapa)

