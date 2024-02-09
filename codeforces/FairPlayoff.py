t = int(input(""))
if t<1 or t>10**4:
    exit(1)
for i in range(t):
    ganhou = []
    jogo = list(map(int, input("").split()))
    if jogo[0]>jogo[1]:
        ganhou.append(jogo[0])
    else:
        ganhou.append(jogo[1])
    if jogo[2]>jogo[3]:
        ganhou.append(jogo[2])
    else:
        ganhou.append(jogo[3])
    resultado=sorted(jogo,reverse=True)
    ganhou=sorted(ganhou,reverse=True)
    if resultado[:2]==ganhou:
        print('YES')
    else:
        print('NO')
