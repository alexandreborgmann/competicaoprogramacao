(valor, dinheiro, bananas ) = map(int, input("").split())
total = 0
for i in range(1,bananas+1):
    total=total+(i*valor)
if total>dinheiro:
    print(total-dinheiro)
else:
    print(0)

