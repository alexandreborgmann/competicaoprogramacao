vezes = int(input(""))
if vezes > 10**4 and vezes < 1:
    exit(1)
for i in range(vezes):
    metros, veloT, veloH = map(int, input("").split())
    t1 = int((metros+veloT-1)/veloT)
    t2 = int((metros+veloH-1)/veloH)
    if t1<=t2:
        print(-1)
    else:
        print(t1-t2-1)
