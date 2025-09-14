t = int(input())
if t<1 or t>4000:
    exit(1)
for i in range(t):
    tamanho = int(input(""))
    a = list(map(int,input("").split()))
    maior = 0
    for i in range(tamanho):
        maior = max(a.count(a[i]), maior)
    print(tamanho-maior)
