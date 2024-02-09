x = int(input(""))
z=-1
while x>z:
    z = int(input(""))
conta = 1
soma = 0
for i in range(x, z+1):
    soma += i
    if soma<=z:
        conta += 1
    #print(i, soma, conta)
print(conta)