import math

vezes = int(input(""))
if vezes<0 or vezes>10**4:
    exit(1)
for j in range(vezes):
    texto = list(input(""))
    #print(texto)
    for i in range(len(texto)):
        if texto[i].isalpha():
            texto[i] = chr(ord(texto[i])+3)
    #print(texto)
    texto = texto[::-1]
    #print(texto)
    tamanho = math.trunc(len(texto)/2)
    for i in range(tamanho,len(texto),1):
        texto[i] = chr(ord(texto[i]) -1)
    resultado=''.join(texto)
    print(resultado)