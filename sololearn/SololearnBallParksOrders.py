'''
Autor: Alexandre Borgmann
Data: 10/04/2020
Sololearn Ballpark Orders

You and three friends go to a baseball game and you offer to go to the concession stand for everyone.
They each order one thing, and you do as well. Nachos and Pizza both cost $6.00.
A Cheeseburger meal costs $10. Water is $4.00 and Coke is $5.00. Tax is 7%.

Task
Determine the total cost of ordering four items from the concession stand.
If one of your friend’s orders something that isn't on the menu, you will order a Coke for them instead.

Input Format
You are given a string of the four items that you've been asked to order that are separated by spaces.

Output Format
You will output a number of the total cost of the food and drinks.

Sample Input
'Pizza Cheeseburger Water Popcorn'

Sample Output
26.75

Você e três amigos vão a um jogo de beisebol e se oferecem para ir ao estande de concessão para todos.
Cada um deles pede uma coisa, e você também. Nachos e Pizza custam US $ 6,00.
Uma refeição com cheeseburger custa US $ 10. A água custa US $ 4,00 e a torta custa US $ 5,00. O imposto é de 7%.

Tarefa
Determine o custo total do pedido de quatro itens do carrinho de concessão.
Se um dos seus amigos pedir algo que não está no menu, você solicitará uma coca-cola para eles.

Formato de entrada
Você recebe uma sequência dos quatro itens solicitados a serem separados por espaços.

Formato de saída
Você produzirá vários custos totais de alimentos e bebidas.

Entrada de amostra
'Pizza Cheeseburger Pipoca de Água'

Saída de amostra
26,75
'''
cardapio = { "Nachos" : 6,
             "Pizza" : 6,
             "Cheeseburger" : 10,
             "Water" : 4,
             "Coke" : 5
          }

linha = input("")
campos = linha.split()
valor=0
for i in campos:
    try:
        valor+=cardapio[i]
    except:
        valor+=cardapio["Coke"]
print("{:.2f}".format(valor+valor*.07))
