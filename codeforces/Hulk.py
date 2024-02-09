numero = int(input(""))
if numero>100 or numero<1:
    exit(1)
i=1
texto = ''
while i < numero:
    if i%2 != 0:
        texto = texto + 'I hate that '
    else:
        texto = texto + 'I love that '
    i = i + 1
if i%2 !=0:
    texto = texto + 'I hate it'
else:
    texto = texto + 'I love it'
print(texto)