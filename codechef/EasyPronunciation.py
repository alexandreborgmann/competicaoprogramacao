vezes = int(input(""))
if vezes > 100 or vezes < 1:
    exit(1)
vogais = ['a','e','i','o','u']
for i in range(vezes):
    n = int(input(""))
    s = input("")
    nconsoantes = 0
    for l in s:
        #print(vogais.count(l),l,nconsoantes)
        if vogais.count(l)!=0:
            nconsoantes=0
        else:
            nconsoantes+=1
        if nconsoantes>=4:
            break
    #print(s,nconsoantes)
    if nconsoantes>=4:
        print('NO')
    else:
        print('YES')
