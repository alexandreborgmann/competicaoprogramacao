'''
Autor: Alexandre Borgmann
Data: 09/04/2020
URI Online Judge | 2787 Xadrez

No tabuleiro de xadrez, a casa na linha 1, coluna 1 (canto superior esquerdo) é sempre branca e as cores das casas se alternam entre branca e
preta, de acordo com o padrão conhecido como... xadrez!
Dessa forma, como o tabuleiro tradicional tem oito linhas e oito colunas, a casa na linha 8, coluna 8 (canto inferior direito) será também
branca. Neste problema, entretanto, queremos saber a cor da casa no canto inferior direito de um tabuleiro com dimensões quaisquer:
L linhas e C colunas. No exemplo da figura, para L = 6 e C = 9, a casa no canto inferior direito será preta!

Entrada
A primeira linha da entrada contém um inteiro L (1 ≤ L ≤ 1000) indicando o número de linhas do tabuleiro.
A segunda linha da entrada contém um inteiro C (1 ≤ C ≤ 1000) representando o número de colunas.
Saída
Imprima uma linha na saída.
A linha deve conter um inteiro, representando a cor da casa no canto inferior direito do tabuleiro: 1, se for branca; e 0, se for preta.

Exemplos de Entrada
6
9

8
8

5
91
Exemplos de Saída
0
1
1
'''
while True:
    linha=int(input(""))
    if(linha<0 or linha>1000):
        print("(1 ≤ L ≤ 1000)")
        continue
    break
while True:
    coluna=int(input(""))
    if(coluna<0 or coluna>1000):
        print("(1 ≤ L ≤ 1000)")
        continue
    break
casa=0
tabuleiro=[]
for i in range(linha):
    dados=[]
    for j in range(coluna):
        if(casa==1):
            casa=0
        else:
            casa=1
        dados.append(casa)
    if(j%2!=0 and i!=linha-1):
        if(casa==1):
            casa=0
        else:
            casa=1
    tabuleiro.append(dados)
      #  print("[{},{}]={}".format(i,j,casa))
'''
for i in range(linha):
    for j in range(coluna):
        print(tabuleiro[i][j],end="")
    print("")
'''
print(casa)

