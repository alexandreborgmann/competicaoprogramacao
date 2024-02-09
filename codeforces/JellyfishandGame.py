vezes = int(input(""))
if vezes<1 or vezes>2000:
    exit(1)
for i in range(vezes):
    appleGellyfish = []
    nJellyfish, nGellyfish, k = map(int, input("").split())
    if nJellyfish>50:
        exit(1)
    if nGellyfish>50:
        exit(1)
    if k<1 and k>10**9:
        exit(1)
    appleJellyfish = list(map(int, input("").split()))
    appleGellyfish = list(map(int, input("").split()))
    appleJellyfish.sort()
    appleGellyfish.sort()
    for i in range(1,k+1):
        if i%2==0: # troca Gellyfish
            if appleJellyfish[-1] > appleGellyfish[0]:
                auxiliar = appleGellyfish[0]
                appleGellyfish[0] = appleJellyfish[-1]
                appleJellyfish[-1] = auxiliar
                appleJellyfish.sort()
                appleGellyfish.sort()
        else: # troca Jellyfish
            if appleGellyfish[-1] > appleJellyfish[0]:
                auxiliar = appleJellyfish[0]
                appleJellyfish[0] = appleGellyfish[-1]
                appleGellyfish[-1] = auxiliar
                appleJellyfish.sort()
                appleGellyfish.sort()

    #print(appleJellyfish)
    print(sum(appleJellyfish))