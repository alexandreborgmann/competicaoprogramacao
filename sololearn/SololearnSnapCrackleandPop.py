'''
Autor: Alexandre Borgmann
Data: 08/04/2020
Sololearn Snap, Crackle and Pop +50 XP

You have six bowls of Rice Krispies in front of you, and they make different noises when you pour milk over them based on the
total number of Rice Krispies in each bowl.
If a bowl has a number of Rice Krispies that is divisible by 3, it will make a Pop sound.
If it is not divisible by 3 but is odd it will make a Snap sound.
If it is not divisible by 3, but it is even, it will make a Crackle sound.

Task:
Based on the quantities in each bowl, output the noise that they make.

Input Format:
You receive 6 integers and each integer represents the number of Rice Krispies in your bowls.

Output Format:
You should output a string with the sounds made by each bowl separated by spaces in the order that they were input.

Sample Input:
18
5
100
25
40
24

Sample Output:
Pop Snap Crackle Snap Crackle Pop

Você tem seis tigelas de Rice Krispies à sua frente, e elas emitem ruídos diferentes quando você derrama leite sobre elas com base no
número total de Krispies de arroz em cada tigela.
Se uma tigela tiver vários Krispies de Arroz divisíveis por 3, emitirá um som pop.
Se não for divisível por 3, mas for ímpar, emitirá um som Snap.
Se não for divisível por 3, mas for par, emitirá um som de Crackle.

Tarefa:
Com base nas quantidades em cada tigela, produza o ruído que elas produzem.

Formato de entrada:
Você recebe 6 números inteiros e cada número inteiro representa o número de arroz Krispies em suas tigelas.

Formato de saída:
Você deve produzir uma sequência com os sons emitidos por cada tigela, separados por espaços na ordem em que foram inseridos.

Entrada de amostra:
18
5
100
25
40.
24

Saída de amostra:
Pop Snap Crackle Snap Crackle Pop
'''
resultado = ""
for i in range(6):
    leitura=float(input(""))
    if(leitura%3==0):
        resultado+="Pop "
    else:
        if(leitura%2==0):
            resultado += "Crackle "
        else:
            resultado += "Snap "
print(resultado)
