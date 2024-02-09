s = input("")
sinteiro = []
for i in range(len(s)):
    if s[i] != '+':
        sinteiro.append(s[i])
sinteiro = sorted(sinteiro)
tamanho=len(sinteiro)
novaString = ""
for i in range(tamanho):
    novaString = novaString + str(sinteiro[i])
    if i!=tamanho-1:
        novaString=novaString+'+'
print(novaString)

