while True:
    n = int(input())
    if n == 0:
        exit(0)
    if n<0 or n>50:
        continue
    pilha = [ i for i in range(n, 0, -1)]

    descartadas = []
    while len(pilha)>=2:
        descartadas.append(pilha.pop())
        pilha.insert(0,pilha.pop())

    print('Discarded cards: ' + ', '.join(map(str,descartadas)))
    print('Remaining card:',pilha[0])