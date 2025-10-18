'''
Autor: Alexandre Borgmann
Data: 22/04/2020
URI Online Judge | 2987 Balão de Honra

Dada uma letra do alfabeto, informe qual a sua posição.
Entrada
Um único caracter L, uma letra maiúscula ('A'-'Z') do alfabeto.
Saída
Um único inteiro, que representa a posição da letra no alfabeto.

Exemplo de Entrada
C
Exemplo de Saída
3
'''

'''
alfabeto = { 'A' : 1,'B' : 2,'C' : 3,'D' : 4,'E' : 5 ,'F' : 6,'G' : 7,'H' : 8 ,'I' : 9,'J' : 10 ,'K' : 11,'L' :  12,
             'M' : 13,'N' : 14,'O' : 15,'P' : 16,'R' : 17,'S' : 18,'T' : 19,'U' : 20 ,'W' : 21,'X' : 22 ,'Y' : 23 ,
             'Z' : 24 }
'''
alfabeto = [ 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letra = input("")
if(letra!=letra.upper() or letra<'A' or letra>'Z'):
    print("'A'-'Z'")
    exit(1)
print(alfabeto.index(letra)+1)
#print(alfabeto[letra])