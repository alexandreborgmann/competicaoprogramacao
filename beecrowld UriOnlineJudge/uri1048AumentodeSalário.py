'''
Autor: Alexandre Borgmann
Data: 10/04/2020
URI Online Judge | 1048 Aumento de Salário

A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário
0 - 400.00
400.01 - 800.00
800.01 - 1200.00
1200.01 - 2000.00
Acima de 2000.00
Percentual de Reajuste
15%
12%
10%
7%
4%
Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.
Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.
Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme exemplo abaixo.

Exemplo de Entrada
400.00
800.01
2000.00
Exemplo de Saída
Novo salario: 460.00
Reajuste ganho: 60.00
Em percentual: 15 %

Novo salario: 880.01
Reajuste ganho: 80.00
Em percentual: 10 %

Novo salario: 2140.00
Reajuste ganho: 140.00
Em percentual: 7 %
'''
salarioAtual = float(input())
if(salarioAtual>0 and salarioAtual<=400):
    percentual=15
elif(salarioAtual>400 and salarioAtual<=800):
    percentual=12
elif(salarioAtual>800 and salarioAtual<=1200):
    percentual=10
elif(salarioAtual>1200 and salarioAtual<=2000):
    percentual=7
elif(salarioAtual>2000):
    percentual=4
else:
    percentual=0
reajuste=salarioAtual*percentual/100.00

print("Novo salario: {:.2f}".format(salarioAtual+reajuste))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {} %".format(percentual))