'''
Autor: Alexandre Borgmann
Data: 08/04/2020
URI Online Judge | 2763 Entrada e Saída CPF

O seu professor gostaria de fazer um programa com as seguintes características:
Leia os dados de um CPF no formato XXX.YYY.ZZZ-DD;
Imprima os quatro números, sendo um valor por linha.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem uma linha.
A linha tem o seguinte formato XXX.YYY.ZZZ-DD, onde XXX, YYY, ZZZ, DD são números inteiros.
Conforme mostrado no exemplo de entrada a seguir.
Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem quatro linhas com um número inteiro em cada uma delas,
conforme foi entrado. Conforme mostra o exemplo de saída a seguir.

Exemplos de Entrada
000.000.000-00

320.025.102-01

Exemplos de Saída
000
000
000
00

320
025
102
01
'''
cpf=input("")
auxiliar=cpf.split("-")
digito=auxiliar[1]
numero=auxiliar[0].split(".",3)
for i in range(3):
    print(numero[i])
print(digito)

