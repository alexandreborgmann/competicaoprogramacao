vezes = int(input(""))
if vezes<1 or vezes>10**3:
    exit(1)
for i in range(vezes):
    nrstr = input("")
    nrInicio = int(nrstr[0]) + int(nrstr[1]) + int(nrstr[2])
    nrFim = int(nrstr[len(nrstr)-3]) + int(nrstr[len(nrstr)-2]) + int(nrstr[len(nrstr)-1])
    if nrInicio!=nrFim:
        print('NO')
    else:
        print('YES')
