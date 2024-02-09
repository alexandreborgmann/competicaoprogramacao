palavra = input("")
palavra=palavra.lower()
lista =list(palavra)
resultado = ''
for i in range(len(lista)):
    if lista[i] not in ('a', 'e','i','o','u','y'):
        resultado=resultado+'.'+lista[i]
print(resultado)
