intervalo, tamanho = map(int, input("").split())
for i in range(1,tamanho+1):
    print(i, sep='', end='')
    if i%intervalo==0:
        print('')
    else:
        print(' ',end='')