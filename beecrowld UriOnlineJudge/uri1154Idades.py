'''
Autor: Alexandre Borgmann
Data: 17/04/2020
URI Online Judge | 1154 Idades

Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo.
O último dado, que não entrará nos cálculos, contém o valor de idade negativa.
Calcular e imprimir a idade média deste grupo de indivíduos.

Entrada
A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.

Saída
A saída contém um valor correspondente à média de idade dos indivíduos.

A média deve ser impressa com dois dígitos após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída
34
56
44
23
-2

39.25
'''
conta = 0
soma = 0
while True:
    a=float(input())
    if(a<0):
        break
    conta+= 1
    soma+=a
print('{:.2f}'.format(soma/conta))
