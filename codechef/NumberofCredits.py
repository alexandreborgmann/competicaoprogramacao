vezes = int(input(""))
if vezes > 10 or vezes < 1:
    exit(1)
for i in range(vezes):
    rtp, audit, nrtp = map(int, input("").split())
    print(4*rtp+2*audit)