'''
Autor: Alexandre Borgmann
Data: 10/04/2020
URI Online Judge | 1038 Lanche

Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
A seguir, calcule e mostre o valor da conta a pagar.

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.
Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

Exemplo de Entrada
3 2
4 3
2 3
Exemplo de Saída
Total: R$ 10.00
Total: R$ 6.00
Total: R$ 13.50
'''
ValorItem = { 1 : 4,
              2 : 4.5,
              3 : 5,
              4 : 2,
              5 : 1.5
            }

linha = input("")
campos = linha.split()
codigo = int(campos[0])
quantidade = int(campos[1])

print("Total: R$ {:.2f}".format(ValorItem[codigo]*quantidade))
