while True:
    try:
        n = int(input(""))
    except EOFError:
        break
    lista = list(map(int, input("").split()))
    maior = max(lista)
    if maior>=20:
        print('3')
    elif maior>=10 and maior<20:
        print('2')
    else:
        print('1')