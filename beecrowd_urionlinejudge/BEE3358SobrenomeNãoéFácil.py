'''
beecrowd | 3358
Sobrenome Não é Fácil
Por Ricardo J. Pfitscher, UNISOCIESC BR Brazil

Timelimit: 1
A região sul do Brasil é caracterizada pela ascendência multicultural de seus habitantes, sendo principalmente europeus e sobretudo italianos, alemães e poloneses. Uma consequência interessante disso é a variação na dificuldade na pronúncia dos sobrenomes da população, o que as vezes dificulta a vida dos professores na realização da chamada de sua turma, gerando até situações constrangedoras. Dada a possibilidade de constrangimento em suas aulas, a professora Jiraiya decidiu pesquisar os sobrenomes em sua lista de chamadas. Na concepção de Jiraiya, um sobrenome é difícil se tiver três ou mais consoantes consecutivas.

Entrada
A entrada contém vários casos de teste. A primeira linha possui um inteiro N que indica o número de casos de teste. Cada caso de teste consiste em um sobrenome. A string contém letras do alfabeto sem acentos, a primeira letra está sempre em maiúscula e o sobrenome pode ter no máximo 42 caracteres.

Saída
Para cada caso de entrada, imprima o sobrenome e se é fácil ou não, conforme mostra o exemplo abaixo.
'''
n = int(input())
for _ in range(n):
    sobrenome = input()
    consoante = 0
    for letra in sobrenome:
        if letra.lower() not in ('a','e','i','o','u'):
            consoante += 1
            if consoante >= 3:
                break
        else:
            consoante = 0
    if consoante >= 3:
        print(f'{sobrenome} nao eh facil')
    else:
        print(f'{sobrenome} eh facil')