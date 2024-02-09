vezes = int(input(""))
if vezes<1 or vezes>10**4:
    exit(1)
for z in range(vezes):
    a, b, c = map(int, input("").split())
    sim = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i+j+k>3:
                    continue
                if a%(i+1) == 0 and b%(j+1) == 0 and c%(k+1) == 0:
                    if a/(i+1) == b/(j+1) and a/(i+1)==c/(k+1):
                        sim =1
                        break
            if sim:
                break
        if sim:
            break
    if sim:
        print('YES')
    else:
        print('NO')


