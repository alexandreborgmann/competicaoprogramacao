'''
Autor: Alexandre Borgmann
Data: 10/04/2020
Sololearn Cheer Creator

You are cheering on your favorite team.
After each play, if your team got over 10 yards further down the field, you stand up and give your friend a high five.
If they don't move forward by at least a yard you stay quiet and say 'shh', and if they move forward 10 yards or less, you say 'Ra!'
for every yard that they moved forward in that play.

Task
Given the number of yards that your team moved forward, output either 'High Five' (for over 10), 'shh' (for <1), or a string that
 has a 'Ra!' for every yard that they gained.

Input Format
An integer value that represents the number of yards gained or lost by your team.

Output Format
A string of the appropriate cheer.

Sample Input
3
Sample Output
Ra!Ra!Ra!

Você está torcendo pelo seu time favorito.
Após cada jogada, se o seu time chegar a mais de 10 jardas abaixo do campo, você se levanta e dê ao seu amigo mais cinco.
Se eles não avançam pelo menos um metro, você fica quieto e diz 'shh', e se eles avançam 10 jardas ou menos, você diz 'Ra!'
para cada quintal que avançaram naquela peça.

Tarefa
Dado o número de jardas que sua equipe avançou, produza 'High Five' (por mais de 10), 'shh' (por <1) ou uma sequência que
  tem um 'Ra!' para cada quintal que eles ganharam.

Formato de entrada
Um valor inteiro que representa o número de jardas obtidas ou perdidas por sua equipe.

Formato de saída
Uma sequência de aplausos apropriados.

Entrada de amostra
3
Saída de amostra
Ra! Ra! Ra!
'''
entrada=int(input(""))
if(entrada<1):
    print('shh')
elif(entrada>10):
    print('High Five')
else:
    print("Ra!"*entrada)
