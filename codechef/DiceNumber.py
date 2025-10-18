vezes = int(input(""))
if vezes > 10**4 and vezes < 1:
    exit(1)
for i in range(vezes):
    dados = list(map(int, input("").split()))

    a = sorted(dados[0:3],reverse=True)
    an = [int(val) for val in a]
    b = sorted(dados[3:], reverse=True)
    bn = [int(val) for val in b]
    #print(an,bn)
    if an>bn:
        print('Alice')
    elif bn>an:
        print('Bob')
    else:
        print('Tie')