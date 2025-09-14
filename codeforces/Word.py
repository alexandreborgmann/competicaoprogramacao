palavra = input("")
nupper=0
nlower=0
for i in range(len(palavra)):
    if ord(palavra[i]) >= 97:
        nlower=nlower+1
    else:
        nupper=nupper+1
if nlower>=nupper:
    print(palavra.lower())
else:
    print(palavra.upper())