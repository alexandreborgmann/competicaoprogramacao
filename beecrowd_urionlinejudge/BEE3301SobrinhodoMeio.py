'''
beecrowd | 3301
Sobrinho do Meio
Por Ricardo Martins, Instituto Federal do Sul de Minas Gerais BR Brazil

Timelimit: 1
Tio Patinhas era um milionário que vivia em sua mansão, e tinha três sobrinhos: Huguinho, Zezinho e Luisinho. Ele se confundia facilmente entre os três sobrinhos, pois eram bem parecidos, apesar de terem idades diferentes. Um dia, os três fizeram uma aposta com o tio: se ele acertasse quem era o sobrinho do meio, ou seja, nem o mais novo, nem o mais velho, eles dariam uma moeda de ouro para ele, e se ele errasse, teria que dar uma moeda de ouro para cada um. Assim, o tio pede a tua ajuda para que ele possa ganhar essa aposta.

Entrada
A entrada consiste em vários casos de teste. Cada caso contém três valores inteiros H, Z e L, que representam as idades de Huguinho, Zezinho e Luisinho, respectivamente.

Saída
Para cada caso de teste imprima o nome do sobrinho do meio, com letras minúsculas.

Exemplos de Entrada	Exemplos de Saída
5 6 7

zezinho

7 5 6

luisinho

6 7 5

huguinho
'''
h, z, l = map(int, input().split())
if h<z and h>l:
    print('huguinho')
if h<l and h>z:
    print('huguinho')
if z<h and z>l:
    print('zezinho')
if z<l and z>h:
    print('zezinho')
if l>h and l<z:
    print('luisinho')
if l<h and l>z:
    print('luisinho')
