distancia = int(input(""))
passos = [ 5, 4 , 3, 2 , 1]
if distancia<1 or distancia>1000000:
    exit(1)
passosfeitos =0
for i in range(len(passos)):
    if passos[i]<=distancia:
        n = (distancia // passos[i])
        passosfeitos = passosfeitos + n
        distancia = distancia - (passos[i]*n)
    if distancia<=0:
        break;
print(passosfeitos)



