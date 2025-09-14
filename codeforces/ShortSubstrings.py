vezes = int(input(""))
if vezes>100 or vezes<1:
    exit(1)
for i in range(vezes):
    a = input("")
    b = ''
    pulo = 0
    for i in range(len(a)):
        if i<len(a)-1 and pulo==0:
            if a[i]==a[i+1]:
                pulo=1
                continue
        b=b+a[i]
        pulo=0
    print(b)
