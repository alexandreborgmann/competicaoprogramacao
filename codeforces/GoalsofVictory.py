vezes = int(input(""))
if vezes<1 or vezes>500:
    exit(1)
for x in range(vezes):
    times = int(input(""))
    jogos = list(map(int, input("").split()))
    print(sum(jogos)*-1)