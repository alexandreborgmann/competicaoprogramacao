'''
beecrowd | 2694
Problema com a Calculadora
Por Neilor Tonin, URI BR Brazil

Timelimit: 1
Joãozinho tem que ajudar seu pai. Um relatório específico com alguns números está saindo com caracteres indesejáveis no meio. A ideia é apenas somar os 3 valores que aparecem em cada linha sempre na mesma posição, ignorando as letras e apresentar esta soma. Não existem espaços em branco na linha.

Entrada
A primeira linha de entrada contém um inteiro N (N < 100000). Seguem N linhas com exatos 14 caracteres que devem ser lidas e delas extraídos e somados os três números existentes.

Saída
Para cada linha de entrada, seu programa deve apresentar um valor numérico inteiro, que é a soma dos 3 números existentes na linha.
'''
n = int(input())
for _ in range(n):
    s = input()
    total = 0
    valor = ""
    for i in range(len(s)):
        if s[i].isdigit():
            valor += s[i]
        else:
            if len(valor)>0:
                total += int(valor)
                valor = ""
    if len(valor) > 0:
        total += int(valor)
    print(total)