linha = input("")
partes = linha.split()
n= int(partes[0])
k = int(partes[1])
if n<2 or n>10**9:
    exit(1)
if k<1 or k>50:
    exit(1)
for i in range(k):
    s=str(n)
    if s[len(s)-1]=='0':
        n=int(n/10)
    else:
        n=n-1
    #print(n,s,i,k)
print(n)
