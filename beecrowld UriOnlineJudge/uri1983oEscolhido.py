'''
Autor: Alexandre Borgmann
Data: 18/04/2020
URI Online Judge | 1984 O Escolhido

As aulas do Prof. Jatobá estão dando o que falar.
Os representantes do MEC vieram até a UNIME de Lauro de Freitas para saber mais detalhes sobre essa nova forma de ensinar Algoritmos.
Além disso, eles queriam selecionar 1 aluno para participar da OBI-Tec (Olimpíada Brasileira de Informática Nível Técnica) e representar a
rede Kroton na competição, pois sabem que lá estão os melhores.
Para selecionar o melhor, eles têm disponível uma lista com o número de inscrição de cada aluno e a sua respectiva nota na disciplina.
Sua tarefa é ajudar o pessoal do MEC a encontrar o aluno mais apto a representar a instituição e quem sabe garantir sua vaga.
Só tem um detalhe, se a nota mais alta não for maior ou igual a 8, você deverá imprimir “Minimum note not reached”.
Entrada
O arquivo contém primeiro a quantidade de alunos (3 <= n <= 100) existentes e em seguida, os n alunos contendo o número da matrícula
(0 < m < 1000000) de cada um, seguido da respectiva nota (0 <= nota <= 10.0, com 1 casa decimal).
Obs.: as notas não serão repetidas. Ou seja, não tem chance de ter dois alunos com a mesma nota.
Saída
Você deve imprimir o número do estudante que obteve a maior pontuação ou "Minimum note not reached" (sem aspas) caso nenhum estudante tenha
 tirado uma nota maior ou igual a 8.

Exemplo de Entrada
3
1000 5
1001 10
1002 6

4
900775 5.7
201553 7.9
5032 6.2
2088 2.1

4
900775 9.4
999999 9.9
10022 9.7
441002 9.8

Exemplo de Saída
1001
Minimum note not reached
999999
'''
alunos = int(input(""))
if(alunos<3 or alunos>100):
    print("3 <= n <= 100");
    exit(0)
maiorNota = 0
for i in range(alunos):
    linha = input("").split()
    codigoAluno = int(linha[0])
    if(codigoAluno<0 or codigoAluno>1000000):
        print("0 < m < 1000000")
        continue
    nota = float(linha[1])
    if(nota<0 or nota>10):
        print("0 <= nota <= 10.0")
        continue
    if(maiorNota<nota):
        maiorNota = nota
        alunoMaiorNota = codigoAluno
if(maiorNota<8):
    print("Minimum note not reached")
else:
    print(alunoMaiorNota)
