'''
beecrowd | 1768
Árvore de Natal
Por Neilor Tonin, beecrowd BR Brazil

Timelimit: 1
As crianças adoram desenhar árvores de natal e você desafiou algumas delas a desenharem árvores de diversos tamanhos com apenas com o caractere asterisco "*".

A regra é simples. De baixo para cima, o tronco da árvore consiste de 3 asteriscos e depois 1. Em seguida vem o restante da árvore, com cada fileira de folhas iniciando no tamanho que você determinou e diminuindo de dois em dois, até chegar na copa da árvore que terá apenas um asterisco. Note que para isso dar certo, somente será permitido tamanhos ímpares para estas árvores.

Entrada
A entrada contém vários casos de teste e termina com EOF. Cada caso de teste consiste em um inteiro N (2 < N < 100).

Saída
Para cada caso de teste de entrada, seu programa deverá desenhar uma árvore conforme especificação acima e exemplo abaixo, com uma linha em branco após cada árvore.
'''
while True:
    try:
        s = input()
        if s == "":
            break
        t = int(s)
        for i in range(1, t + 1, 2):
            espaco = int((t - i) / 2)
            print(' ' *  espaco + '*' * i)
            #+ ' ' *  espaco)
        metade = t // 2
        print(' ' * metade + '*')
        print(' ' * (metade - 1) + '***')
        print()
    except (EOFError, ValueError):
        break
