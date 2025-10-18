soma = 0
i = 0
while True:
    nota = float(input(""))
    if nota == 2:
        exit(0)
    if nota<0 or nota>10:
        print('nota invalida')
    else:
        i += 1
        soma += nota
        if i == 2:
            print('media = {:.2f}'.format(soma/2))
            while True:
                executa = input("")
                print('novo calculo (1-sim 2-nao)')
                if executa == '1':
                    break
                if executa == '2':
                    exit(0)
            i = 0
            soma = 0
