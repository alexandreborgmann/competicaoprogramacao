vezes = int(input(""))
if vezes > 150 or vezes < 1:
    exit(1)
x=0
for i in range(vezes):
    linha = input("")
    if linha=='X++' or linha=='++X':
        x = x + 1
    else:
        x = x - 1
print(x)