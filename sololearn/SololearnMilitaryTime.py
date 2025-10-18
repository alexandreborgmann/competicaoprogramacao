'''
Autor: Alexandre Borgmann
Data: 19/04/2020
Sololearn Military Time

You want to convert the time from a 12 hour clock to a 24 hour clock.
If you are given the time on a 12 hour clock, you should output the time as it would appear on a 24 hour clock.

Task:
Determine if the time you are given is AM or PM, then convert that value to the way that it would appear on a 24 hour clock.

Input Format:
A string that includes the time, then a space and the indicator for AM or PM.

Output Format:
A string that includes the time in a 24 hour format (XX:XX)

Sample Input:
1:15 PM

Sample Output:
13:15
'''
linha = input("").split(" ")
formato = linha[1].upper()
horaMinuto = linha[0].split(":")
hora = int(horaMinuto[0])
minuto = horaMinuto[1]
if formato=="PM":
    hora += 12
print("{:02d}:{}".format(hora,minuto))

