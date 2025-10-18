n = int(input())
for j in range(1,n+1):
    led = 0
    x = input()
    for i in range(0,len(x)):
        if x[i] == '1':
            led = led + 2
        if x[i] == '2':
            led = led + 5
        if x[i] == '3':
            led = led + 5
        if x[i] == '4':
            led = led + 4
        if x[i] == '5':
            led = led + 5
        if x[i] == '6':
            led = led + 6
        if x[i] == '7':
            led = led + 3
        if x[i] == '8':
            led = led + 7
        if x[i] == '9':
            led = led + 6
        if x[i] == '0':
            led = led + 6
    print('{} leds'.format(led))

'''

estou tomando runtime error que nem sei o que baita bugado pois no pycharm roda
vezes = int(input(""))
if vezes<1 or vezes>1000:
    exit(1)
leds = { '1' : 2,
         '2' : 5,
         '3' : 5,
         '4' : 4,
         '5' : 5,
         '6' : 6,
         '7' : 3,
         '8' : 7,
         '9' : 6,
         '0' : 6
}

for i in range(vezes):
    numero = input("")
    quantidadeLeds = 0
    for j in numero:
        quantidadeLeds = quantidadeLeds + leds.get(j)
    print('{} leds'.format(quantidadeLeds))




        if j=='1':
            quantidadeLeds += 2
        elif j=='2':
            quantidadeLeds += 5
        elif j=='3':
            quantidadeLeds += 5
        elif j=='4':
            quantidadeLeds += 4
        elif j=='5':
            quantidadeLeds += 5
        elif j=='6':
            quantidadeLeds += 6
        elif j=='7':
            quantidadeLeds += 3
        elif j=='8':
            quantidadeLeds += 7
        elif j=='9':
            quantidadeLeds += 6
        elif j=='0':
            quantidadeLeds += 6
'''