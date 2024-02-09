palavra = input("")
if len(palavra)>100 or len(palavra)<1:
    exit(1)
listaUnica = []
listaUnica.append(palavra[0])
for i in range(len(palavra)):
    if palavra[i] not in listaUnica:
        listaUnica.append(palavra[i])

if (len(listaUnica)-1)%2==0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
