'''
beecrowd | 2591
HameKameKa
Por Ricardo Martins, IFSULDEMINAS BR Brazil

Timelimit: 1
O Hamekameka foi inventado por Mestre Hame praticado por cinquenta anos antes de conhecer Kogu. Chamando sua energia latente nas palmas de suas mãos, Hame consegue lançar um raio explosivo de energia. Kogu aprende após ver Mestre Hame usando-o para apagar as chamas na casa de um Rei. Para a surpresa de Hame, Kogu consegue performar a técnica de primeira, embora seja apenas forte o suficiente para destruir o carro que Chamya deu para Mulba. Kogu descobriu que há um padrão na pronúncia correta deste ataque, de modo que, se não for pronunciado corretamente, o mesmo não acontece.

Escreva um programa que, dada a parte inicial de um Hamekameka, faça a finalização ideal para que o ataque seja realizado com sucesso.

Entrada
A entrada começa com um valor C, indicando a quantidade de casos de teste. Em seguida, temos C linhas, cada uma com o início de um ataque, com, no máximo, 200 letras.

Saída
Para cada caso de teste, imprima a finalização adequada, para que o ataque se concretize.
'''
c = int(input())

for _ in range(c):
    s = input().strip()

    # Encontra os grupos de 'a'
    partes = s.split('m')
    # partes[0] contém "haaa...", partes[1] contém "ekaaa..."

    # Conta 'a' na primeira parte (depois do h)
    x = partes[0].count('a')

    # Conta 'a' na segunda parte (depois do k)
    # A segunda parte começa com "eka", então procuramos após o 'k'
    segunda_parte = partes[1]
    pos_k = segunda_parte.find('k')
    y = segunda_parte[pos_k + 1:].count('a')

    print('k' + 'a' * (x * y))