'''
Autor: Alexandre Borgmann
Data: 11/04/2020
Sololearn Izzy the Iguana

Your pet Iguana has run away, and you found it up in a tree!
It will come down right away if you brought the right snacks, but if you don't have enough, you will have to wait.
You need 10 total snack points to bring it down.
Lettuce is worth 5, Carrot is worth 4, Mango is worth 9, and Cheeseburger is worth 0.

Task:
Evaluate whether or not you have enough snack points to convince your iguana to come down.

Input Format:
Your input is a string that represents the snacks that you have.
Snacks are separated by spaces, you can have any number of snacks, and they can repeat.

Output Format:
A string that says 'Come on Down!' if you have enough points, or 'Time to wait' if you do not.

Sample Input:
Mango Cheeseburger Carrot

Sample Output:
Come on Down!
'''
produtos = {"Lettuce": 5,
             "Carrot" :4,
             "Mango": 9,
             "Cheeseburger": 0
}
linha = input("")
entradas = linha.split()
soma=0
for i in range(len(entradas)):
    soma+=produtos[entradas[i]]
if(soma>10):
    print("Come on Down!")
else:
    print("Time to wait")

