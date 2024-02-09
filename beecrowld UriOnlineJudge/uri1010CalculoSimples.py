'''
Autor: Alexandre Borgmann
Data: 01/04/2020
URI Online Judge | 1010 Cálculo Simples

Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2.
Após, calcule e mostre o valor a ser pago.
Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.
Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.
Exemplos de Entrada/Exemplos de Saída
12 1 5.30
16 2 5.10
VALOR A PAGAR: R$ 15.50
13 2 15.30
161 4 5.20
VALOR A PAGAR: R$ 51.40
1 1 15.10
2 1 15.10
VALOR A PAGAR: R$ 30.20
'''

linha1 = input("")
linha2 = input("")
campos1 = linha1.split()
campos2 = linha2.split()

CodigoPeca1 = int(campos1[0])
NumeroPecas1 = int(campos1[1])
ValorUnitarioPecas1 = float(campos1[2])

CodigoPeca2 = int(campos2[0])
NumeroPecas2 = int(campos2[1])
ValorUnitarioPecas2 = float(campos2[2])

ValorPagar = NumeroPecas1*ValorUnitarioPecas1 + NumeroPecas2*ValorUnitarioPecas2

print('VALOR A PAGAR: R$ {:.2f}'.format(ValorPagar))
