'''
Autor: Alexandre Borgmann
Data: 09/04/2020
URI Online Judge | 2949 A Sociedade do Anel

Frodo era um pequeno hobbit (pessoinhas pequenas e de pés peludos) que vivia tranquilamente no Condado, tomando seus vários cafés da manhã
recheados de muitos alimentos suculentos que a dieta de um bom hobbit proporciona.
Certo dia, seu tio Bilbo lhe entrega seu famoso anel dourado, e Gandalf, um mago muito “bacanudo”, diz a Frodo que esse anel não era normal e
que deveria ser jogado na Montanha da Perdição, para que um grande mal fosse evitado.
Para essa jornada, foi formada uma comitiva, composta de anões, elfos, humanos, hobbits e magos.
Frodo deseja saber a quantidade de cada raça que irá com ele para a jornada.
Dada uma lista das pessoas que se alistaram, faça um relatório para Frodo da comitiva.
Entrada
A primeira linha da entrada é composta por um inteiro N(0 < N <= 10), indicando o número de pessoas que se alistaram.
Cada uma das próximas N linhas seguintes são compostas por uma cadeia de caracteres (sem espaços e de caracteres alfanuméricos apenas) e um
caractere maiúsculo, indicando, respectivamente, o nome e o tipo da raça do respectivo ser.
Este caractere poderá ser:
● A - Para anões;
● E - Para elfos;
● H - Para humanos;
● M - Para magos;
● X - Para hobbits (X, pois todo hobbit é uma incógnita para o mundo).
Saída
Deve ser apresentado um relatório com a comitiva do Frodo, indicando em cada linha quantos seres de cada espécie estarão na jornada, seguindo
a ordem: hobbits, humanos, elfos, anões e magos.

Exemplo de Entrada
9
Frodo X
Gandalf M
Pippin X
Sam X
Aragorn H
Legolas E
Gimli A
Boromir H
Merry X
Exemplo de Saída
4 Hobbit(s)
2 Humano(s)
1 Elfo(s)
1 Anao(es)
1 Mago(s)

'''
especie = { "Hobbit" : 0,
             "Humano" : 0,
             "Elfo" : 0,
             "Anao" : 0,
             "Mago" : 0
          }
codigoEspecie = { "X" : "Hobbit",
                  "H" : "Humano",
                  "E" :"Elfo",
                  "A" : "Anao",
                  "M" : "Mago"
               }

codigo = ("Hobbit","Humano","Elfo","Anao","Mago")

nome = []

n = int(input(""))
for i in range(n):
    nome.append(input(""))
    especie[codigoEspecie[nome[i][len(nome[i])-1]]]+=1

for i in range(5):
    if codigo[i]=='Anao':
        print("{} {}(oes)".format(especie[codigo[i]], codigo[i]))
    else:
        print("{} {}(s)".format(especie[codigo[i]],codigo[i]))
