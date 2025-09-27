nrcasos = int(input())
for z in range(nrcasos):
    nrfrase = int(input())
    idiomas = {}
    for i in range(nrfrase):
        f = input()
        idiomas[f] = idiomas.get(f, 0) + 1
    qtd = len([lingua for lingua in idiomas.values() if lingua != 'ingles' ])
    if len(idiomas) == 1:
        print(list(idiomas.keys())[0])
    else:
        print('ingles')

