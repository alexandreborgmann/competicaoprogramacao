vezes = int(input(""))
if vezes > 100 or vezes < 1:
    exit(1)
facil=0
resposta = list(map(int, input("").split()))
for i in range(vezes):
    if resposta[i]==1:
        facil = 1
        break
if facil==0:
    print('EASY')
else:
    print('HARD')
