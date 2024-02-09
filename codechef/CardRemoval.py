t = int(input())
if t<1 or t>100:
    exit(1)
for i in range(t):
    n = int(input(""))
    cartas = list(map(int,input("").split()))
    conta = [0]*n
    for j in range(n):
        conta[j] = cartas.count(cartas[j])
    print(n-max(conta))