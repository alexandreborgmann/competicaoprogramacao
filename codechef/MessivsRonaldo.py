messiGol, messiAssist, ronaldoGol, ronaldoAssist = map(int, input("").split())
messiTotal=messiGol*2+messiAssist
ronaldoTotal=ronaldoGol*2+ronaldoAssist
if messiTotal>ronaldoTotal:
    print('Messi')
elif ronaldoTotal>messiTotal:
    print('Ronaldo')
else:
    print('Equal')