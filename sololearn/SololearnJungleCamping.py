'''
Autor: Alexandre Borgmann
Data: 11/04/2020
Sololearn Jungle Camping +10 XP

You are camping alone out in the jungle and you hear some animals in the dark nearby.
Based on the noise they make, determine which animals they are.

Task:
You are given the noises made by different animals that you can hear in the dark, evaluate each noise to determine which animal
it belongs to. Lions say 'Grr', Tigers say 'Rawr', Snakes say 'Ssss', and Birds say 'Chirp'.

Input Format:
A string that represent the noises that you hear with a space between them.

Output Format:
A string that includes each animal that you hear with a space after each one. (animals can repeat)

Sample Input:
Rawr Chirp Ssss

Sample Output:
Tiger Bird Snake
'''
animais = {"Lion" : "Grr",
            "Tiger" : "Rawr",
            "Snake" : "Ssss",
             "Bird":  "Chirp"
}

linha = input("")
entradas = linha.split()
for i in range(len(entradas)):
    for a in animais:
        if(entradas[i].find(animais[a])!=-1):
            print(a,end=" ")
print("")
