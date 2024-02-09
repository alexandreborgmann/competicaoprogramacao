horaInicio, minutoInicio, horaFim, minutoFim = map(int, input("").split())
if horaInicio > horaFim:
    hora = (24-horaInicio)+horaFim
elif horaFim > horaInicio:
    hora = horaFim - horaInicio
elif horaInicio == horaFim:
    if minutoInicio == minutoFim:
        hora = 24
    else:
        hora = 0
if minutoInicio > minutoFim:
    minuto = (60-minutoInicio)+minutoFim
    if hora>0:
        hora = hora - 1
    elif hora==24:
        hora = 23
elif minutoFim > minutoInicio:
    minuto = minutoFim - minutoInicio
elif minutoInicio == minutoFim:
    minuto = 0
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora,minuto))
