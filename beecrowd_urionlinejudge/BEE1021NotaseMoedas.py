'''
beecrowd | 1021
Notas e Moedas
Por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
'''
valor = float(input())
centavos = int(valor * 100 + 0.001)
print('NOTAS:')
n100 = centavos // 10000
centavos %= 10000
print(f"{n100} nota(s) de R$ 100.00")
n50 = centavos // 5000
centavos %= 5000
print(f"{n50} nota(s) de R$ 50.00")
n20 = centavos // 2000
centavos %= 2000
print(f"{n20} nota(s) de R$ 20.00")
n10 = centavos // 1000
centavos %= 1000
print(f"{n10} nota(s) de R$ 10.00")
n5 = centavos // 500
centavos %= 500
print(f"{n5} nota(s) de R$ 5.00")
n2 = centavos // 200
centavos %= 200
print(f"{n2} nota(s) de R$ 2.00")
print('MOEDAS:')
m1 = centavos // 100
centavos %= 100
print(f"{m1} moeda(s) de R$ 1.00")
m50 = centavos // 50
centavos %= 50
print(f"{m50} moeda(s) de R$ 0.50")
m25 = centavos // 25
centavos %= 25
print(f"{m25} moeda(s) de R$ 0.25")
m10 = centavos // 10
centavos %= 10
print(f"{m10} moeda(s) de R$ 0.10")
m5 = centavos // 5
centavos %= 5
print(f"{m5} moeda(s) de R$ 0.05")
print(f"{centavos} moeda(s) de R$ 0.01")
