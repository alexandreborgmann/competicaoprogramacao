'''
Autor: Alexandre Borgmann
Data: 07/04/2020
URI Online Judge | 2581 I am Toorg!

Toorg é o integrante mais sábio do grupo de heróis denominado Os Protetores da Via Láctea.
Para qualquer pergunta, ele tem a resposta ideal! Escreva um programa que, dada uma pergunta, informe a resposta de Toorg.
Entrada
A entrada terá diversos casos de teste.
A cada caso de teste, um número N é apresentado, que representa o número de casos de teste.
Em seguida, haverá N linhas, com as perguntas feitas para Toorg.
Saída
Para cada caso de teste, imprima a resposta de Toorg.

Exemplo de Entrada
3
Who are you?
How old are you?
What can I do for you?
Exemplo de Saída
I am Toorg!
I am Toorg!
I am Toorg!
'''
n = int(input())
for i in range(n):
    lecaso = input()
    print("I am Toorg!")
