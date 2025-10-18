'''
beecrowd | 1278
Justificador II
Por Bruno Santos  Brasil

Timelimit: 1
Nós temos alguns textos e queremos formatá-los e justificá-los à direita, ou seja, alinhar suas linhas à margem direita de cada um. Crie um programa que, após ler um texto, reimprima esse texto com apenas um espaço entre as palavras e suas linhas justificadas à direita em todo o texto.

Entrada
A entrada contém diversos casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 100) que indica o número de linhas de texto que virão a seguir. Cada uma destas N linhas de texto contém de 1 a 50 letras maiúsculas (‘A’-‘Z’) ou espaços (‘ ’). Todas as linhas de texto contém no mínimo uma letra. Poderá haver mais de um espaço entre as palavras. É também possível haver espaços no início e no final da linha. O fim da entrada é indicado por N = 0.

Saída
Para cada caso de teste imprima o texto com apenas um espaço entre as palavras, e inserindo tantos espaços quanto forem necessários à esquerda de cada linha do texto, para que elas apareçam alinhadas à margem direita daquele texto, e na mesma ordem da entrada. Deixe uma linha em branco entre os casos de testes. Não imprima espaços no final de cada linha, nem espaços desnecessários à esquerda, de modo que pelo menos uma das linhas impressa em cada texto inicie com uma letra.


'''
primeiro_caso = True
while True:
    n = int(input())
    if n == 0:
        break
    if not primeiro_caso:
        print()
    primeiro_caso = False
    textos = []
    for i in range(n):
        linha = map(str, input().split())
        primeira = True
        linha_atual = ""
        for palavra in linha:
            if primeira:
                primeira = False
            else:
                linha_atual = linha_atual + ' '
            linha_atual = linha_atual + palavra
        textos.append(linha_atual)
    tamanho_maximo = len(max(textos, key=len))
    for i in range(n):
        print(f"{textos[i]:>{tamanho_maximo}}")

