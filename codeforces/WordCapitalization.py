palavra = input("")
if len(palavra)>10**3 or len(palavra)<1:
    exit(1)
if ord(palavra[0])>=97:
    palavra=chr(ord(palavra[0])-32)+palavra[1:]
print(palavra)