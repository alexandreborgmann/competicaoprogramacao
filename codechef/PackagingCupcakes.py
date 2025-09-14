vezes = int(input(""))
if vezes > 1000 and vezes < 1:
    exit(1)
for i in range(vezes):
    n = int(input(""))
    maior=0
    resto=0
    for i in range(1,n+1):
        x= int(n/i)
        if i>maior and resto<=n-(x*i):
            maior = i
            resto = n-(x*i)
    print(maior)