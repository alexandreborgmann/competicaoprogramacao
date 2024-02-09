'''
Autor: Alexandre Borgmann
Data: 11/04/2020
Sololearn Safety Deposit Boxes

You are robbing a bank, but you’re not taking everything.
You are looking for a specific item in the safety deposit boxes and you are going to drill into each one in order to find your item.
Once you find your item you can make your escape, but how long will it take you to get to that item?

Task
Determine the amount of time it will take you to find the item you are looking for if it takes you 5 minutes to drill into each box.

Input Format
A string that represent the items in each box that will be drilled in order (items are separated by a comma), and secondly,
a string of which item you are looking for.

Output Format
An integer of the amount of time it will take for you to find your item.

Sample Input
'gold,diamonds,documents,Declaration of Independence,keys'
'Declaration of Independence'

Sample Output
20

Você está roubando um banco, mas não está pegando tudo.
Você está procurando um item específico nos cofres e vai detalhar cada um deles para encontrar seu item.
Depois de encontrar o item, você pode escapar, mas quanto tempo leva para chegar a ele?

Tarefa
Determine a quantidade de tempo que você levará para encontrar o item que está procurando, se você levar 5 minutos para
perfurar cada caixa.

Formato de entrada
Uma sequência que representa os itens em cada caixa que serão perfurados em ordem (os itens são separados por vírgula) e,
em segundo lugar, uma sequência do item que você está procurando.

Formato de saída
Um número inteiro da quantidade de tempo que levará para você encontrar seu item.

Entrada de amostra
'ouro,diamantes,documentos,Declaração de independência,chaves'
'Declaração de independência'

Saída de amostra
20
'''
tempo=5
linha=input("")
itens=linha.split(",")
caixa=input("")
for i in itens:
#    print(i," ",tempo)
    if(i==caixa):
        break
    tempo+=5
print(tempo)