vezes = int(input(""))
if vezes > 100000 or vezes < 1:
    exit(1)
anton=0
danik=0
linha = input("")
for i in range(len(linha)):
    if linha[i]=='A':
        anton = anton + 1
    else:
        danik = danik +1
if anton>danik:
    print('Anton')
elif danik>anton:
    print('Danik')
else:
    print('Friendship')