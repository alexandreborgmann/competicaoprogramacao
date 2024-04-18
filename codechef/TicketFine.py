t = int(input())
if  t<1 or t>10:
    exit(1)
for i in range(t):
    valor, passageiro, total = map(int, input().split())
    print(abs(total-passageiro)*valor)