'''
Autor: Alexandre Borgmann
Data: 18/04/2020
URI Online Judge | 2165 Tuitando

O microblog Twitter é conhecido por limitar as postagens em 140 caracteres.
Conferir se um texto vai caber em um tuíte é sua tarefa.
Entrada
A entrada é uma linha de texto T (1 ≤ |T| ≤ 500).
Saída
A saída é dada em uma única linha. Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres.
Se T tem mais de 140 caracteres, a saída deve ser "MUTE".

Exemplo de Entrada
RT @TheEllenShow: If only Bradley's arm was longer. Best photo ever. #oscars pic.twitter.com/C9U5NOtGap
Exemplo de Saída
TWEET
'''
linha = input("")
if(len(linha)==0 or len(linha)>500):
    print("(1 ≤ |T| ≤ 500)")
    exit(0)
if(len(linha)<=140):
    print("TWEET")
else:
    print("MUTE")
