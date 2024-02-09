n = int(input(""))
soma = 0
for i in range(1,n+1):
    soma = soma + (i* (1 if i%2==0 else -1))
print(soma)