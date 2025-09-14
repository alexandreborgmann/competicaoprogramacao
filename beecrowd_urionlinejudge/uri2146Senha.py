'''
Author: Alexandre Borgmann
Date: 6/4/2020
URI Online Judge | 2146 Senha

Sr. Amnésio tinha uma grande dificuldade em guardar senhas.
Para lembrá-las, ele sempre usava números, e as escrevia em pedaços de papel, que também perdia com facilidade, fazendo com que ele precisasse
modificar a senha cada vez que isto acontecia.
Cansado, ele pensou em uma forma mais prática: colocava no papel um número próximo da senha, depois ele usava sempre uma mesma conta para
lembrar a senha, baseada no número escrito no papel.
Mas ele também esquecia a fórmula, por isto, pediu para você escrever um programa que, dado o número do papel, informe a senha correspondente.
Escreva um programa que, dado um número, informe a respectiva senha.
Entrada
A entrada terá diversos casos de teste. A cada caso de teste, terá um número N, que representa o número escrito no papel (1001 ≤ N ≤ 9999).
A entrada termina com o fim do arquivo.
Saída
Para cada caso de teste, imprima a senha correspondente.
Em todos os casos, a fórmula será a mesma, igual aos exemplos abaixo.

Exemplo de Entrada
1234
2000
1001
9999
Exemplo de Saída
1233
1999
1000
9998
'''
while True:
    try:
        senha = int(input(""))
    except:
        break
    if(senha==-1):
        break
    if(senha<1001 or senha>9999):
        continue
    print(senha-1)
