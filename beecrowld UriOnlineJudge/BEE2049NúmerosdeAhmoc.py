instancia = 1
while True:
    artista = input('')
    if artista == '0':
        break
    if instancia>1:
        print()
    print('Instancia',instancia)
    linha = input('')
    if artista in linha:
        print('verdadeira')
    else:
        print('falsa')
    instancia += 1



