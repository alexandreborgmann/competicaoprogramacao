inicio, fim = map(int, input("").split())
if inicio > fim:
    resultado = (24-inicio)+fim
elif fim > inicio:
    resultado = fim - inicio
elif inicio == fim:
    resultado = 24
print('O JOGO DUROU {} HORA(S)'.format(resultado))