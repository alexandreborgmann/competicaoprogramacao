from typing import List

def soma(n: int, a: List[int]):
    esquerda, direita = [0]*n,[0]*n
    esquerda[0] = a[0]
    direita[n-1] = a[n-1]

    for i in range(1, n):
        esquerda[i] = max(esquerda[i - 1], a[i])
        direita[n - i - 1] = max(direita[n - i], a[n - i - 1])

    soma = 0
    for i in range(n):
        soma += min(esquerda[i],direita[i])
    #print(a,esquerda,direita)
    print(soma)

vezes = int(input(""))
if vezes > 10**5 and vezes < 1:
    exit(1)
for z in range(vezes):
    n = int(input(""))
    a = list(map(int, input("").split()))
    soma(n, a)

