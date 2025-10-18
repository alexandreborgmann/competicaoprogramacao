'''
Autor: Alexandre Borgmann
Data: 08/04/2020
Sololearn Popsicles

You have a box of popsicles and you want to give them all away to a group of brothers and sisters.
If you have enough left in the box to give them each an even amount you should go for it!
If not, they will fight over them, and you should eat them yourself later.

Task
Given the number of siblings that you are giving popsicles to, determine if you can give them each an even amount or
if you shouldn't mention the popsicles at all.

Input Format
Two integer values, the first one represents the number of siblings, and the second one represents the number of popsicles
that you have left in the box.

Output Format
A string that says 'give away' if you are giving them away, or 'eat them yourself' if you will be eating them yourself.

Sample Input
3 9

Sample Output
give away

Você tem uma caixa de picolés e deseja entregá-los a um grupo de irmãos e irmãs.
Se você tiver o suficiente na caixa para dar a cada um valor igual, você deve fazê-lo!
Caso contrário, eles lutarão por eles, e você deve comê-los você mesmo mais tarde.

Tarefa
Dado o número de irmãos aos quais você está dando picolés, determine se você pode dar a cada um uma quantia par ou
se você não mencionar os picolés.

Formato de entrada
Dois valores inteiros, o primeiro representa o número de irmãos e o segundo representa o número de picolés
que você deixou na caixa.

Formato de saída
Uma string que diz 'doar' se você estiver doando ou 'coma você mesmo' se você o estiver comendo.

Entrada de amostra
3 9

Saída de amostra
doar
'''

irmaos=int(input(""))
picoles=int(input(""))
if(picoles%irmaos==0):
    print("give away")
else:
    print("eat them yourself")