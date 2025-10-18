vezes = int(input(""))
if vezes<0 or vezes>100:
    exit(1)
somaSaque = 0
somaBloqueio = 0
somaAtaque = 0
somaSaqueOk = 0
somaBloqueioOk = 0
somaAtaqueOk = 0
for j in range(vezes):
    jogador = input("")
    saque, bloqueio, ataque = map(int, input("").split())
    saqueOk, bloqueioOk, ataqueOk = map(int, input("").split())
    somaSaque += saque
    somaBloqueio += bloqueio
    somaAtaque += ataque
    somaSaqueOk += saqueOk
    somaBloqueioOk += bloqueioOk
    somaAtaqueOk += ataqueOk

print('Pontos de Saque: {:.2f} %.'.format((somaSaqueOk*100)/somaSaque))
print('Pontos de Bloqueio: {:.2f} %.'.format((somaBloqueioOk*100)/somaBloqueio))
print('Pontos de Ataque: {:.2f} %.'.format((somaAtaqueOk*100)/somaAtaque))