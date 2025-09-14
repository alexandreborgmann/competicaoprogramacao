n = int(input(""))
s = input("")
soma = 0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        soma=soma+1
print(soma)