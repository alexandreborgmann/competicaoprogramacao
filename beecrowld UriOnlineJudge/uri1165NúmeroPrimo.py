'''
Author: Alexandre Borgmann
Date: 4/2/2020
URI Online Judge | 1165 Número Primo

Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo.
Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

Entrada
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada.
Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

Saída
Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”, de acordo com a especificação fornecida.

Exemplo de Entrada
3
8
51
7
Exemplo de Saída
8 nao eh primo
51 nao eh primo
7 eh primo
'''
while True:
    QuantidadeLer = int(input())
    if(QuantidadeLer>=1 and QuantidadeLer<=100):
        break
    print(" N (1 ≤ N ≤ 100)")

for i in range(QuantidadeLer):
    valor = int(input())
    primo = 0
    for j in range(2,valor+1):
        if(valor%j==0 and valor!=j):
            primo = 1
            print(valor,'nao eh primo')
            break
    if(not primo):
        print(valor,"eh primo")
