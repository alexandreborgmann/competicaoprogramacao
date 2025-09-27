'''
beecrowd | 1255
Frequência de Letras
Por Sumudu Fernando  Canadá

Timelimit: 1
Neste problema estamos interessados na frequência das letras em uma dada linha de texto.

Especificamente, deseja-se saber qual(is) a(s) letra(s) de maior frequência do texto, ignorando o “case sensitive”, ou seja maiúsculas ou minúsculas (sendo mais claro, “letras” referem-se precisamente às 26 letras do alfabeto).

Entrada
A entrada contém vários casos de teste. A primeira linha contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de uma única linha de texto. A linha pode conter caracteres “não letras”, mas é garantido que tenha ao menos uma letra e que tenha no máximo 200 caracteres no total.

Saída
Para cada caso de teste, imprima uma linha contendo a(s) letra(s) que mais ocorreu(ocorreram) no texto em minúsculas (se houver empate, imprima as letras em ordem alfabética).
'''
n = int(input())
for i in range(n):
    frase = input().lower()
    alfabeto = {chr(i): 0 for i in range(97, 123)}
    for letra in frase:
        if letra in alfabeto:
            alfabeto[letra] += 1
    maior_freq = max(alfabeto.values())
    letras_mais_frequentes = "".join(letra for letra, freq in alfabeto.items() if freq == maior_freq)
    print(letras_mais_frequentes)
