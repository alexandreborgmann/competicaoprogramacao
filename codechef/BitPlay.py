vezes = int(input(""))
if vezes > 3000 or vezes < 1:
    exit(1)
MOD = 10 ** 9 + 7
for i in range(vezes):
    tamanho = int(input(""))
    s = input("")
    retorno = 1
    for j in range(0,tamanho-2,2):

        x = 0
        a = int(s[j])
        b = int(s[j+1])
        c = int(s[j+2])

        if ((a&b)==c):
            x += 1
        if  ((a|b)==c):
            x += 1
        if ((a^b)==c):
            x += 1

        retorno *= x
        retorno %= MOD
    print(retorno)
