vezes = int(input(""))
if vezes > 100 or vezes < 1:
    exit(1)
resultado=0
for i in range(vezes):
    pessoas, capacidade = map(int, input("").split())
    if (capacidade-pessoas)>=2:
        resultado+=1
print(resultado)
