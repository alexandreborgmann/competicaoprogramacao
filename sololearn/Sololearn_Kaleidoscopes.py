'''
Autor: Alexandre Borgmann
Data: 08/04/2020
Sololearn Kaleidoscopes

You sell souvenir kaleidoscopes at a gift shop, and if a customer buys more than one, they get a 10% discount on all of them!
Given the total number of kaleidoscopes that a customer buys, let them know what their total will be. Tax is 7%.
All of your kaleidoscopes cost the same amount, 5.00.

Task:
Take the number of kaleidoscopes that a customer buys and output their total cost including tax and any discounts.

Input Format:
An integer value that represents the number of kaleidoscopes that a customer orders.

Output Format:
A number that represents the total purchase price to two decimal places.

Sample Input:
4

Sample Output:
19.26

Você vende caleidoscópios de lembrança em uma loja de presentes e, se um cliente comprar mais de um, ele receberá um
desconto de 10% em todos eles!
Dado o número total de caleidoscópios que um cliente compra, informe-o sobre o total.
O imposto é de 7%.
Todos os seus caleidoscópios custam a mesma quantia, 5,00.

Tarefa:
Pegue o número de caleidoscópios que um cliente compra e produza seu custo total, incluindo impostos e quaisquer descontos.

Formato de entrada:
Um valor inteiro que representa o número de caleidoscópios que um cliente solicita.

Formato de saída:
Um número que representa o preço total da compra com duas casas decimais.

Entrada de amostra:
4

Saída de amostra:
19,26
'''
percentualDesconto=0
preco=5.00
quantidade=int(input(""))
if(quantidade>=2):
    percentualDesconto=10
venda=quantidade*preco
desconto=(venda*percentualDesconto/100.00)
vendaLiquida=(venda-desconto)
valorComImposto=vendaLiquida+(vendaLiquida*.07)
print("{:.2f}".format(valorComImposto))
