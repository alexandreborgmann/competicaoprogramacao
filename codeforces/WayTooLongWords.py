vezes = int(input(""))
if vezes>100 or vezes<1:
    exit(1)
for i in range(vezes):
    palavra = input("")
    if len(palavra)<=10:
        print(palavra)
    else:
        print(f'{palavra[0]}{len(palavra)-2}{palavra[-1]}')