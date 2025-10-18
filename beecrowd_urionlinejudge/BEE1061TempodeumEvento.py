lista = list(map(str,input("").split(" ")))
diaInicio = int(lista[1])

lista = list(map(str,input().split(" ")))
horaInicio = int(lista[0])
minutoInicio = int(lista[2])
segundoInicio = int(lista[4])

lista = list(map(str,input("").split(" ")))
diaFim = int(lista[1])

lista = list(map(str,input().split(" ")))
horaFim = int(lista[0])
minutoFim = int(lista[2])
segundoFim = int(lista[4])

dia = diaFim - diaInicio
hora = horaFim - horaInicio
minuto = minutoFim - minutoInicio
segundo = segundoFim - segundoInicio
if segundo<0:
    segundo += 60
    minuto -= 1
if minuto<0:
    minuto += 60
    hora -= 1
if hora<0:
    hora += 24
    dia -= 1

print('{} dia(s)'.format(dia))
print('{} hora(s)'.format(hora))
print('{} minuto(s)'.format(minuto))
print('{} segundo(s)'.format(segundo))
