vezes = int(input(""))
if vezes<1 or vezes>1440:
    exit(1)
for z in range(vezes):
    hora, minuto = map(int, input("").split(":"))

    if hora >= 12:
        s = 'PM'
        if hora>=13:
            hora -= 12
    elif hora <12:
        s = 'AM'
        if hora == 0:
            hora = 12
    print(f"{hora:02}:{minuto:02} {s}")