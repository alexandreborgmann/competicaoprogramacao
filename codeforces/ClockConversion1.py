vezes = int(input(""))
if vezes<1 or vezes>1440:
    exit(1)
for z in range(vezes):
    hora, minuto = map(int, input("").split(":"))
    s = 'AM'
    if hora > 11:
        s = 'PM'
    if hora == 0 or hora == 12:
        hora = 12
    else:
        hora = hora % 12
    print(f"{hora:02}:{minuto:02} {s}")