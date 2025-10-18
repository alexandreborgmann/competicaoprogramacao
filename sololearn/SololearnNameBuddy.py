'''
Autor: Alexandre Borgmann
Data: 18/04/2020
Sololearn Name Buddy

You are grouped into groups for a project, and you are supposed to come up with as many famous scientists who have the same first
letter of their name as you as possible.
Will you have to come up with the answers on your own, or is there somebody in your group that you can work with?

Task:
Determine if anyone in your group has the same first letter of their name as you.

Input Format:
A string of your group members' names separated by spaces, and then a string of your name.

Output Format:
A string that says 'Compare notes' if you have a name buddy, or 'No such luck' if you have to work on this alone.

Sample Input:
Becky Joan Fred Trey
Brad

Sample Output:
Compare notes
'''
linha = input("")
nomes = linha.split()
meuNome = input("")
for i in nomes:
    if(meuNome[0]==i[0]):
        print("Compare notes")
        exit(0)
print("No such luck")

