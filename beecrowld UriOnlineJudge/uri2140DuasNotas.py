'''
Author: Alexandre Borgmann
Date: 6/4/2020
URI Online Judge | 2140  Duas Notas

Gilberto é um famoso vendedor de esfirras na região.
Porém, apesar de todos gostarem de suas esfirras, ele só sabe dar o troco com duas notas, ou seja, nem sempre é possível receber o troco certo. Para facilitar a vida de Gil, escreva um programa para ele que determine se é possível ou não devolver o troco exato utilizando duas notas.
As notas disponíveis são: 2, 5, 10, 20, 50 e 100.
Entrada
A entrada deve conter o valor inteiro N da compra realizada pelo cliente e, em seguida, o valor inteiro M pago pelo cliente (N < M ≤ 104).
 A entrada termina com N = M = 0.
Saída
Seu programa deverá imprimir "possible" se for possível devolver o troco exato ou "impossible" se não for possível.

Exemplo de Entrada
11 23
500 650
100 600
9948 9963
1 2
2 4
0 0
Exemplo de Saída
possible
possible
impossible
possible
impossible
impossible
'''
notas = [2,5,10,20,50,100]
while True:
    try:
        linha = input("")
        campos = linha.split()
        compra = int(campos[0])
    except:
        compra=0
    try:
        pagamento = int(campos[1])
    except:
        pagamento=0
    if( compra==0 and pagamento==0):
        break
 #   if(pagamento<compra or pagamento>10000):
 #       print("valor invalido")
 #       continue
    troco=pagamento-compra
    achou=0
    for i in range(6):
        for j in range(6):
            if(troco==notas[i]+notas[j]):
                achou=1

    if(achou==0):
        print("impossible\n",end="")
    else:
        print("possible\n",end="")