'''
Autor: Alexandre Borgmann
Data: 09/04/2020
URI Online Judge | 2791 Feijão

Conta-se nos arredores de Montes Claros que, há muito tempo no mercado municipal, Sebastião e seus companheiros de trabalho sempre jogam uma
partida de adivinhação após a entrega dos produtos agrícolas colhidos na semana que se passou.
O jogo, que se chama Adivinhe Onde o Feijão Está'', consiste em esconder um grão de feijão em um de quatro copos opacos e, depois de
embaralhá-los, o apostador deve adivinhar em qual copo o legume está.
Neste ano, devido ao grande sucesso cultural e histórico e à enorme quantidade de pessoas que praticam este jogo no mercado municipal, a
prefeitura resolveu realizar um campeonato de Adivinhe Onde o Feijão Está''.
Entretanto, ela necessita de um programa para mostrar aos expectadores onde o feijão estava após o fim de uma partida.
Sabendo que a próxima Maratona Mineira de Programação ocorrerá na cidade, ela logo encomendou uma solução aos exímios programadores.
Desta forma, você deve auxiliar a organização nesta missão com um programa que informe, ao fim de uma partida, onde o feijão esteve.
Entrada
A entrada conterá apenas uma linha com quatro inteiros, C1,C2,C3 e C4
separados por um espaço. Haverá sempre exatamente um copo com o feijão.

Exemplos de Entrada
0 0 0 1
0 1 0 0
0 0 1 0
Exemplos de Saída
4
2
3
'''
vetor = []
posicao=0
linha = input("")
campos = linha.split()
for i in range(4):
    vetor.append(int(campos[i]))
    if(vetor[i]==1):
        posicao=i+1
print(posicao)