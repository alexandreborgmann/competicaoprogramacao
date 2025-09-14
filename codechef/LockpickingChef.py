vezes = int(input(""))
if vezes > 10**4 and vezes < 1:
    exit(1)
for i in range(vezes):
    tamsenha, tamsegredo = map(int, input("").split())
    senha = input("")
    segredo = input("")
    move=0
    for i in range(len(senha)):
        if senha[i,i+tamsegredo-1]==segredo:
            break
        else:
            move +=1
    minimo=move
    for i in range(len(senha),1):
        if senha[i,i+tamsegredo-1]==segredo:
            break
        else:
            move +=1

