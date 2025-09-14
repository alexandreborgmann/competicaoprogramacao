'''
Author: Alexandre Borgmann
Date: 5/4/2020
URI Online Judge | 1985 MacPRONALTS

O MacPRONALTS está com uma super promoção, exclusivo para os competidores da primeira Seletiva do MaratonaTEC.
Só que teve um problema, todos os maratonistas foram tentar comprar ao mesmo tempo, com isso gerou uma fila muito grande.
O pior é que a moça do caixa estava sem calculadora ou um programa para ajudá-la a calcular com maior agilidade, eis que surge
você para fazer um programa para ajudar a coitada e aumentar a renda do MacPRONALTS.
Segue o cardápio do dia contendo o número do produto e seu respectivo valor.
1001 | R$ 1.50
1002 | R$ 2.50
1003 | R$ 3.50
1004 | R$ 4.50
1005 | R$ 5.50
Entrada
A primeira entrada informada é a quantidade de produtos comprados (1 <= p <= 5).
Para cada produto segue a quantidade (1 <= q <= 500) que o consumidor comprou.
Obs.: não poderão ser informados números de produtos repetidos.
Saída
Você deve imprimir o valor da compra com duas casas decimais.

Input Sample
2
1001 2
1005 3

1
1003 500

5
1001 500
1005 300
1003 23
1002 52
1004 44

Output Sample
19.50
1750.00
2808.50
'''
Preco = {1001: 1.50,1002 :2.50,1003 : 3.50,1004 : 4.50,1005: 5.50}
Compra = {1001: 0,1002:0,1003: 0,1004: 0,1005: 0}
while True:
    ItensComprados=int(input(""))
    if(ItensComprados<0 or ItensComprados>5):
        print("Itens invalidos deve ser 1-5")
        continue
    break

ValorCompra=0
for i in range(ItensComprados):
    linha = input("")
    campos = linha.split()

    CodigoProduto=int(campos[0])
    QuantidadeComprada=int(campos[1])
    if(QuantidadeComprada<1 or QuantidadeComprada>500):
        print("Quantidade invalida 1 <= q <= 500")
    else:
        if(Compra[CodigoProduto]==0):
            Compra[CodigoProduto]=QuantidadeComprada
            ValorCompra+=(Preco[CodigoProduto]*QuantidadeComprada)
        else:
            print("Produto ja comprado")

print("{:.2f}".format(ValorCompra))
