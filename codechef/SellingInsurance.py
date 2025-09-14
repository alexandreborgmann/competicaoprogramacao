import math

vezes = int(input(""))
if vezes > 100 and vezes < 1:
    exit(1)
for i in range(vezes):
    seguro = int(input(""))
    comissao = seguro*.20
    print(math.ceil(100/comissao))