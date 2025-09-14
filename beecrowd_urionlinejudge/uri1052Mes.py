'''
Autor: Alexandre Borgmann
Data: 02/04/2020
URI Online Judge | 1052 Mês

Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

Entrada
A entrada contém um único valor inteiro.

Saída
Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.

Exemplo de Entrada	Exemplo de Saída
4

April
'''
MesExtenso = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

while True:
    mes = int(input())
    if(mes>=1 and mes<=12):
      break;
    print("Informe um mês válido em numero entre 1-12")

print(MesExtenso[mes-1].capitalize())



