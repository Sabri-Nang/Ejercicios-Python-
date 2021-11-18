#inclusive

frase='todos somos programadores'
frase_final=''
palabras=frase.split()

for palabra in palabras:
    if palabra[-2:]=='os' or palabra[:-2]=='as':
        frase_final+=palabra[:-2]+'es'+' '
    elif palabra[-1:]=='o' or palabra[-1:]=='a':
        frase_final+=palabra[:-1]+'e'
    else:
        frase_final+=palabra+' '
print(frase_final)


        