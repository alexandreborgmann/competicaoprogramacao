def primo(n):
    for i in range(n,-1,-1):
        if n%i==0:
            return(0)
    return(1)

vezes = int(input(""))
if vezes > 10**5 and vezes < 1:
    exit(1)
jogador=0
for z in range(vezes):
    n = int(input())
    while n!=0 and primo(n):
        n = n
        if jogador

if jogador == 0:
    print('Bob')
else:
    print('Alice')