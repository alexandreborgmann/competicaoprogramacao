'''
Autor: Alexandre Borgmann
Data: 10/04/2020
URI Online Judge | 1020 Idade em Dias

Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias.
Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364.
Este é apenas um exercício com objetivo de testar raciocínio matemático simples.
Entrada
O arquivo de entrada contém um valor inteiro.
Saída
Imprima a saída conforme exemplo fornecido.

Exemplo de Entrada
400
800
30
Exemplo de Saída
1 ano(s)
1 mes(es)
5 dia(s)

2 ano(s)
2 mes(es)
10 dia(s)

0 ano(s)
1 mes(es)
0 dia(s)
'''
import math

idadeDias = int(input(""))
if(idadeDias>=365):
    ano=math.trunc(idadeDias/365)
    idadeDias-=ano*365
else:
    ano=0
if(idadeDias>=30):
    mes=math.trunc(idadeDias/30)
    idadeDias-=mes*30
else:
    mes=0
dia=idadeDias

print("{} ano(s)".format(ano))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dia))