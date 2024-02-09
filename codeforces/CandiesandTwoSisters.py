vezes = int(input(""))
if vezes > 10**4 or vezes < 1:
    exit(1)
for z in range(vezes):
    n = int(input(""))
    i = n
    j = 1
    soma = 0
    for i in range(n,1,-1):
        for j in range(i-1,0,-1):
            if i+j == n:
                soma += 1
                #print('igual',i,j,soma)
            #print(i,j,soma)
    print(soma)
