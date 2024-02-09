'''
Autor: Alexandre Borgmann
Data: 05/04/2020
URI Online Judge | 1924 Vitória e a Indecisão

Está para nascer alguém mais indeciso do que Vitória.
Apesar dela saber que é uma ótima programadora, daquelas que possui projetos na área de TI publicados e diversos
outros em andamento, ela não tem certeza se vai seguir na área.
Há noites que ela diz que não quer Computação, há dias que ela diz que quer alguma Engenharia, em outros ela quer
qualquer outro curso, já chegou até a pensar em algum de Humanas, que pecado!
Mas você está aqui pra ajudá-la.
A sua tarefa é bem simples, será dado uma lista com diversos nomes de cursos de graduação e você terá que imprimir o
nome do curso que Vitória deve fazer.
Entrada
A primeira linha de entrada contém um inteiro 1 ≤ n ≤ 2000, que representa a quantidade de cursos a serem considerados. Cada uma das próximas n linhas irá conter uma cadeia de caracteres S, 1 ≤ |S| ≤ 100, representando o nome do curso.
Saída
Imprima o nome do curso que Vitória deve fazer, sem acentuação.

Exemplos de Entrada
3
Ciencia da Computacao
Engenharia Eletrica
Matematica
3
Sociologia
Filosofia
Fisica

Exemplos de Saída
Ciencia da Computacao
Ciencia da Computacao
'''
while True:
    n = int(input(''))
    if(n<1 or n>2000):
        print("Digite entre N(1 ≤ N ≤ 2000")
        conintue
    break

for i in range(n):
    curso=input("")
    while True:
        if(len(curso)<1 or len(curso)>100):
            print("Tamanho inválido S, 1 ≤ | S | ≤ 100")
            continue
        break
print("Ciencia da Computacao")





