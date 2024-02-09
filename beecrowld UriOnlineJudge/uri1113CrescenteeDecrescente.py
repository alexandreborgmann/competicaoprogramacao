'''
Author: Alexandre Borgmann
Date: 4/4/2020
URI Online Judge | 1113 Crescente e Decrescente

Leia uma quantidade indeterminada de duplas de valores inteiros X e Y.
Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.
Entrada
A entrada contém vários casos de teste.
Cada caso contém dois valores inteiros X e Y.
A leitura deve ser encerrada ao ser fornecido valores iguais para X e Y.
Saída
Para cada caso de teste imprima “Crescente”, caso os valores tenham sido digitados na ordem crescente, caso contrário imprima a mensagem “Decrescente”.

Exemplo de Entrada
5 4
7 2
3 8
2 2
Exemplo de Saída
Decrescente
Decrescente
Crescente
'''
while True:
    linha = input("")
    campos = linha.split()

    x = int(campos[0])
    y = int(campos[1])
    if(x==y):
        break
    if(x>y):
        print("Decrescente")
    elif y>x:
        print("Crescente")
