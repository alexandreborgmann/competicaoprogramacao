a = int(input(""))
if a<-1000 or a>1000:
    exit(-1)
b = int(input(""))
if b<-1000 or b>1000:
    exit(-1)
operacao = input("")
if operacao not in ("+", "-", "*", "/"):
    exit(1)
if operacao=='+':
    print(a+b)
elif operacao=='-':
    print(a-b)
elif operacao=='*':
    print(a*b)
elif operacao=='/':
    print(a/b)