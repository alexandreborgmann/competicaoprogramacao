'''
Author: Alexandre Borgmann
Date: 7/4/2020
URI Online Judge | 2172  Evento

Prog e Cackto começaram recentemente a jogar um jogo de RPG chamado Fortaleza.
Neste, para o jogador evoluir de nível o mesmo precisa derrotar monstros, nos quais dá um valor de experiência (XP) para o jogador.
A produtora do jogo, Jogos Extremos, anunciou que na próxima semana irá realizar o primeiro evento XP no qual aumentará a experiência dos monstros em X vezes.
Como Prog e Cackto estão em um nível muito alto no qual os monstros tem um valor muito alto de pontos de experiência, eles estão tendo dificuldades de calcular a quantidade de pontos de experiência que
os monstros terão durante o evento. Você pode ajudá-los?

Entrada
Haverá diversos casos de teste. Cada caso de teste contém dois valores X (0 < X ≤ 3) indicando o valor de aumento da EXP dos monstros e M (10 ≤ M ≤ 232-1) indicando o valor de EXP do monstro.
A entrada termina com os valores X == 0 e M == 0, nos quais não devem ser processados.

Saída
Para cada caso, seu programa deverá mostrar um valor E, referente ao novo EXP do monstro.

Exemplo de Entrada
1 544768710
2 538533133
3 38884958
0 0
Exemplo de Saída
544768710
1077066266
116654874
'''
while True:
    try:
        linha = input("")
        campos = linha.split()
        x= int(campos[0])
        if(x<0 or x>3):
            print("x deve ser entre 0-3")
            continue
    except:
        x=0
    try:
        m = int(campos[1])
        if((m<10 or m>2**32) and m!=0):
            print('x deve ser  M (10 ≤ M ≤ 232-1)')
    except:
        m=0
    if(x==0 and m==0):
        break
    print("{}".format(m*x))
