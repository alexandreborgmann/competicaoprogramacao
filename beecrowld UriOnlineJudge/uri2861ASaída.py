'''
Autor: Alexandre Borgmann
Data: 09/04/2020
URI Online Judge | 2861 A Saída

Cacunda, Bizz e Massacote são amigos inseparáveis.
Na faculdade, em alguns dias, não iam à aula para jogar truco.
Certo dia, um professor estava passando perto deles.
Na mesma hora, os três gritaram bem alto a palavra “gzuz”.
Após esse grito, ficaram invisíveis, e o professor não os viu.
Outra vez, a turma deles estava respondendo perguntas do professor.
Quando era a vez de algum deles, respondiam com a palavra “gzuz”, e o professor aceitava como resposta e dava a nota máxima da pergunta.
Faça a simulação da saída que eles encontraram para se safar dos mais diversos problemas.
Entrada
A entrada é composta por vários casos de teste.
A primeira linha contém um número inteiro C (2 <= C <= 99) relativo ao número de perguntas que o professor fez.
As C linhas seguintes vêm com uma pergunta feita pelo professor.
Saída
Para cada pergunta, imprima a resposta que foi dita pelos três amigos.

Exemplo de Entrada
3
What is output?
What is your name?
Where is the book?
Exemplo de Saída
gzuz
gzuz
gzuz

VIII Olimpíada Interna de Programação do IFSULDEMINAS - OLIP 2018
'''
while True:
    n=int(input(""))
    if(n<=2 or n>100):
        print("(2 <= C <= 99)")
        continue
    break
for i in range(n):
    pergunta=input("")
    print("gzuz")
