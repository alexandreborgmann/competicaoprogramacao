'''
Autor: Alexandre Borgmann
Data: 07/04/2020
URI Online Judge | 2748 Saída 2

O seu professor de programação gostaria de fazer uma tela com as seguintes características:
Ter 39 traços (-) na primeira linha;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, embaixo do 10 traço deve começar a escrever a palavra
"Roberto" e o restante preencher no meio com espaço em branco;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, preencher no meio com espaço em branco;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, embaixo do 10 traço deve começar a escrever o número
"5786" e o restante preencher no meio com espaço em branco;
Repita o procedimento 3;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, embaixo do 10 traço deve começar a escrever a palavra "UNIFEI"
e o restante preencher no meio com espaço em branco;
Repita o procedimento 1.
No final deve ficar igual a imagem a seguir:
--------------------------------------- (39 traços)
|        Roberto                      |
|                                     |
|        5786                         |
|                                     |
|        UNIFEI                       |
--------------------------------------- (39 traços)
Entrada
Não há.
Saída
A saída será impresso conforme a figura acima.
'''
print("-"*39)
print("|        Roberto                      |")
print("|"+" "*37+"|")
print("|        5786                         |")
print("|"+" "*37+"|")
print("|        UNIFEI                       |")
print("-"*39)
