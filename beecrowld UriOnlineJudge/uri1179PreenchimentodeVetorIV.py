'''
Autor: Alexandre Borgmann
Data: 17/04/2020
URI Online Judge | 1179 Preenchimento de Vetor IV

Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares.
Só que o tamanho de cada um dos dois vetores é de 5 posições.
Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos.
Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar.
Cada vetor pode ser preenchido tantas vezes quantas for necessário.

Entrada
A entrada contém 15 números inteiros.

Saída
Imprima a saída conforme o exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
1
3
4
-4
2
3
8
2
5
-7
54
76
789
23
98

par[0] = 4
par[1] = -4
par[2] = 2
par[3] = 8
par[4] = 2
impar[0] = 1
impar[1] = 3
impar[2] = 3
impar[3] = 5
impar[4] = -7
impar[0] = 789
impar[1] = 23
par[0] = 54
par[1] = 76
par[2] = 98
'''
def MostraVetor(vetor,tipo):
    for i  in range(len(vetor)):
        print("{}[{}] = {}".format(tipo,i,vetor[i]))

par = []
impar = []
contaPar = 0
contaImpar = 0
for i in (range(15)):
    valor = int(input())
    if(valor%2==0):
        par.append(valor)
        contaPar+=1
        if(contaPar==5):
            MostraVetor(par,"par")
            par.clear()
            contaPar = 0
    else:
        impar.append(valor)
        contaImpar+=1
        if(contaImpar==5):
            MostraVetor(impar,"impar")
            impar.clear()
            contaImpar = 0
if(contaImpar!=0):
    MostraVetor(impar, "impar")
if(contaPar!=0):
    MostraVetor(par, "par")



