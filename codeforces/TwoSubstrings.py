s = input("")
#s = 'ABAXXXAB'
resultado = 'NO'
temp = s
if s.find('AB') != -1:
    s = s.replace('AB','',1)
    if s.find('BA') != -1:
        resultado = 'YES'
if resultado == 'NO':
    if temp.find('BA') != -1:
        temp = temp.replace('BA', '', 1)
        if temp.find('AB') != -1:
            resultado = 'YES'
print(resultado)