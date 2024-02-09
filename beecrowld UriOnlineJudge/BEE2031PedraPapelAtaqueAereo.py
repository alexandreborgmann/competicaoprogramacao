vezes = int(input(""))
if vezes > 1000 or vezes < 1:
    exit(1)
for i in range(vezes):
    jogador1 = input("")
    jogador2 = input("")

    if jogador1 == jogador2:
        if jogador1 == 'papel':
            resultado ='Ambos venceram'
        if jogador1 == 'pedra':
            resultado ='Sem ganhador'
        if jogador1 == 'ataque':
            resultado = 'Aniquilacao mutua'
    else:
        if (jogador1 == 'ataque' and jogador2 == 'pedra') or \
            (jogador1 == 'pedra' and jogador2 == 'papel') or \
            (jogador1 == 'ataque' and jogador2 == 'papel'):
            resultado = 'Jogador 1 venceu'
        else:
            resultado = 'Jogador 2 venceu'

    print(resultado)
