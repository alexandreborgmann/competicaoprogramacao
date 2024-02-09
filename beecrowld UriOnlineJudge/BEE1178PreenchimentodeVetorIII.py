valor = float(input(""))
n = [0]*100
for i in range(100):
    n[i] = valor
    valor /= 2
    print('N[{}] = {:.4f}'.format(i,n[i]))