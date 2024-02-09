'''
Autor: Alexandre Borgmann
Data: 11/04/2020
Sololearn Roadrunner +50 XP

A coyote is chasing a roadrunner and they start out 50 feet apart.
If you know how fast they are both traveling, and how far the roadrunner is from safety, determine whether or not the coyote is
able to catch the roadrunner.
Both animals and the roadrunner's safe place are on a straight line.

Task:
Determine whether or not the roadrunner made it to safety.

Input Format:
Three integer values, the first value represents the distance the roadrunner is from safety, then the roadrunner's
speed (feet/second) and then the coyote's speed (feet/second).

Output Format:
A string that says 'Meep Meep' if the roadrunner made it, or 'Yum' if the coyote caught up to the roadrunner.

Sample Input:
10
5
20

Sample Output:
Meep Meep

Um coiote está perseguindo um papa-léguas e eles começam a 15 metros de distância.
Se você sabe o quão rápido eles estão viajando e a que distância o corredor está da segurança, determine se o coiote é ou não
capaz de pegá-lo.
Os animais e o local seguro do papa-léguas estão em linha reta.

Tarefa:
Determine se o roadrunner chegou ou não à segurança.

Formato de entrada:
Três valores inteiros, o primeiro valor representa a distância que o roadrunner está da segurança, a velocidade do roadrunner
(pés / segundo) e a velocidade do coiote (pés / segundo).

Formato de saída:
Uma string que diz 'Meep Meep' se o roadrunner conseguiu, ou 'Yum' se o coiote o alcançou.

Entrada de amostra:
10
5
20

Saída de amostra:
Meep Meep
'''
distanciaSegura = int(input(""))
velocidadeRunner = int(input(""))
velocidadeCoiote = int(input(""))

finalRunner=(distanciaSegura)/velocidadeRunner
finalCoiote=((15+distanciaSegura)/velocidadeCoiote)
#print(finalRunner,' ',finalCoiote)
if(finalRunner<finalCoiote):
    print("Meep Meep")
else:
    print("Yum")