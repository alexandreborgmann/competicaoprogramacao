'''
Crie três variáveis para armazenar números inteiros;
Leia o primeiro número, que pode ser um valor na faixa de: -10000 ≤ A ≤ 10000;
Leia o segundo número, que pode ser um valor na faixa de: 0 ≤ B ≤ 99;
Leia o terceiro número, que pode ser um valor na faixa de: 0 ≤ C ≤ 999;
Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na primeira variável, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na segunda variável, uma virgula, um espaço em branco, a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na terceira variável. Não esqueça de pular linha;
Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e justificado a direita;
Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e preenchido com zeros;
Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e justificado a esquerda.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem três linhas. Na primeira linha tem um inteiro A (-10000 ≤ A ≤ 10000). Na segunda linha tem um inteiro B (0 ≤ B ≤ 99). Na terceira linha tem um inteiro C (0 ≤ C ≤ 999). Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem quatro linhas da forma descrita no item 5. Conforme mostra o exemplo de saída a seguir.
'''
a = int(input(""))
if a > 10000 or a < -10000:
    exit(1)
b = int(input(""))
if b > 99 or b < 0:
    exit(1)
c = int(input(""))
if b > 999 or b < 0:
    exit(1)

print(f"A = {a}, B = {b}, C = {c}")
print(f"A = {a:>10}, B = {b:>10}, C = {c:>10}")
print(f"A = {a:010}, B = {b:010}, C = {c:010}")
print(f"A = {a:<10}, B = {b:<10}, C = {c:<10}")
