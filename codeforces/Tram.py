vezes = int(input(""))
if vezes<1 or vezes>1000:
    exit(1)
dentro=0
maior=0
for i in range(vezes):
    saiu, entrou = map(int, input("").split())
    if saiu>dentro:
        saiu=dentro
    dentro=dentro+entrou-saiu
    if maior<dentro:
        maior=dentro
    #print(saiu,entrou,dentro)
print(maior)