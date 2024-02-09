matriz = [0]*5
for i in range(5):
    matriz[i] = list(map(int, input("").split()))
umLinha=0
umColuna=0
for i in range(5):
    for j in range(5):
        if matriz[i][j]==1:
            umLinha=i
            umColuna=j
            break
print(abs(2-umLinha)+abs(2-umColuna))

