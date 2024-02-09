'''
Author: Alexandre Borgmann
Date: 4/5/2020
URI Online Judge | 1188 Área Inferior

Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12].
Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão na área inferior da matriz,
conforme ilustrado abaixo (área verde).

Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá
ser realizada com os elementos da matriz.
Seguem os 144 valores de ponto flutuante de dupla precisão (double) que compõem a matriz.
Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

Exemplo de Entrada
S
1.0
330.0
-3.5
2.5
4.1
...
Exemplo de Saída
112.4
'''
import math

LINHA=3
COLUNA=3
matriz = []

while True:
    operacao = (input("")).upper()
    if(operacao not in ('S','M')):
        print("Informe o caracter (S)oma ou (M)edia")
        continue
    break
conta = 1
for i in range(LINHA):
    linha = []
    for j in range(COLUNA):
        valor = conta #float(input(""))
        linha.append(valor)
        conta+=1
    matriz.append(linha)
soma=0
conta=0
for i in range(LINHA):
    for j in range(COLUNA):
        #print("[{},{}] {}".format(i,j,matriz[i][j]))
        if i>math.trunc(LINHA/2) and (j>math.trunc(COLUNA/2)):
            #print("somou ",matriz[i][j])
            soma+=matriz[i][j]
            conta+=1
if(operacao=='S'):
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/conta))
#print(matriz)