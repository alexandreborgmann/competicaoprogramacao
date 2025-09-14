vezes = int(input(""))
if vezes > 10**4 or vezes < 1:
    exit(1)
for i in range(vezes):
    linha = input("")
    partes = linha.split()
    n = float(partes[0])
    k = float(partes[1])
    if k > 10 ** 18 or k < 1 or k==2:
        exit(1)
    achou = 0
    x = n
    while x>=0 and achou == 0:
        y = n
        #print('x=',x,'k=',k)
        while y >= 0 and achou == 0:
            #print('x=',x,'y=',y,'r ',2*x,'+',k*y,'=',2*x + k*y,'k=',k,'n=',n)
            if 2*x + k*y == n:
                print('YES')
                achou = 1
            y = y - 1
        x = x - 1
    if achou==0:
        print('NO')
