vezes = int(input(""))
if vezes<1 or vezes>3*10**5:
    exit(1)
for x in range(vezes):
    n = int(input(""))
    i = 0
    resultado = []
    while n>0:
        tamanho = len(str(n))-1
        valor = (n // 10**tamanho)*(10**tamanho)
        resultado.append(valor)
        n -= valor
        i += 1
        #print('i=',i,'tamanho=',tamanho,10**tamanho,'valor=',valor,'n=',n)
    print(i)
    for i in range(len(resultado)):
        print(resultado[i],end=' ')
    print()
