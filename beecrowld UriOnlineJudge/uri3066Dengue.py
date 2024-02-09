'''
Autor: Alexandre Borgmann
Data: 10/04/2020
URI Online Judge | 3066 Dengue

A Costa do Mosquito é um país pequeno mas paradisíaco.
Todos os habitantes têm boas moradias, bons empregos, o clima é agradável, e os governantes são justos e incorruptíveis.
O sistema de transporte público da Costa do Mosquito é composto de uma rede de linhas de trem. O sistema foi projetado de forma peculiar:
existe um único percurso ligando duas quaisquer vilas (esse percurso possivelmente passa por outras vilas).
Por exemplo, na figura abaixo, que mostra um trecho do mapa da Costa do Mosquito, há apenas um percurso entre as vilas A e C, passando pelas
vilas B, G e D. Uma tarifa fixa de M$ 1,00 é cobrada por cada viagem entre vilas vizinhas; assim, para uma viagem de A a C o usuário gasta
M$ 4,00.
Devido a um inesperado surto de dengue, o Ministério da Saúde da Costa do Mosquito resolveu montar um Posto de Vacinação.
Para evitar que habitantes gastem muito dinheiro para se deslocar até a vila onde ficará o Posto de Vacinação, o Ministério da Saúde
decidiu que este deverá ser instalado em uma vila de forma que o gasto com transporte até o Posto, para os habitantes que gastarem mais,
seja o menor possível (para o caso da figura abaixo a vila escolhida seria G).
Sua tarefa é escrever um programa que determine uma vila onde deve ser instalado o Posto de Vacinação.
Esta vila deve ser tal que o custo com transporte, para os habitantes que tiverem maior custo, seja o menor possível.
Note que devido à característica peculiar do sistema viário, ou haverá uma única vila que satisfaz essa restrição, ou haverá duas vilas
que a satisfazem. No caso de existirem duas vilas apropriadas, qualquer uma delas serve como solução.
Entrada
A entrada é composta de vários conjuntos de teste. A primeira linha de um conjunto de testes contém um número inteiro N (0 ≤ N ≤ 100) que indica
a quantidade de vilas do país.
As vilas são numeradas de 1 a N. As N-1 linhas seguintes contêm, cada uma, dois inteiros positivos X e Y que indicam que a vila X tem um
caminho que a liga diretamente com a vila Y, sem passar por outras vilas. O final da entrada é indicado por N = 0.
Saída
Para cada conjunto de teste da entrada seu programa deve produzir três linhas na saída.
A primeira linha deve conter um identificador do conjunto de teste, no formato “Teste n”, onde n é numerado a partir de 1.
A segunda linha deve conter o número da vila na qual deve ser instalado o Posto de Vacinação.
A terceira linha deve ser deixada em branco.
A grafia mostrada no Exemplo de Saída, abaixo, deve ser seguida rigorosamente.

Exemplo de Entrada
2
1 2
7
1 2
2 5
7 4
7 2
4 6
3 4
1
0 0
Exemplo de Saída
Teste 1
1
Teste 2
7
Teste 3
1
'''
contaTeste=1
while True:
    try:
        n = int(input(""))
    except:
        n=0
    if(n==0):
        break
    if(n<0 or n>100):
        print("0 ≤ Xi ≤ 100")
        continue

    for i in range(n):
        linha=input("")
        campos=linha.split()

    print("Teste {}".format(contaTeste))
    print("")
    contaTeste+=1