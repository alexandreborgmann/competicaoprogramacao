while True:
    n, m = map(int, input("").split())
    if m<=0 or n<=0:
        exit(0)
    if n>m:
        menor = m
        maior = n
    else:
        menor = n
        maior = m

    soma = 0
    for i in range(menor,maior+1):
        soma += i
        print(i,' ',end='',sep='')
    print('Sum={}'.format(soma))
