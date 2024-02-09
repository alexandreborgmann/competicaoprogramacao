'''
Autor: Alexandre Borgmann
Data: 19/04/2020
Sololearn How Far?

You are walking from your house to a pond that is down your street.
How many blocks over will you have to walk until you get to the pond?

Task:
Evaluate how many blocks you will have to walk if you are given a representation of your street where H represents your house,
P represents the pond, and every B represents a block in between the two.

Input Format:
A string of letters representing your house, the pond, and blocks on your street.

Output Format:
An integer value that represents the number of blocks between your house and the pond.

Sample Input:
BBHBBBBPBBB

Sample Output:
4
'''
achouCasa = 0
blocos = 0
achouLago = 0
linha = input("").upper()
for letra in linha:
    if(letra=='P'):
        achouLago=1
    if(letra=='H'):
        achouCasa = 1
    if ((achouCasa==1 and achouLago==0) or
        (achouCasa==0 and achouLago==1)
    ):
        if letra== 'B':
            blocos+=1
if achouCasa==1 and achouLago==1:
    print(blocos)

