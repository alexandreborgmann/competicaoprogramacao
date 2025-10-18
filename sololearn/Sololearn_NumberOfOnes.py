'''
Autor: Alexandre Borgmann
Data: 10/04/2020
Sololearn Number of Ones

Task:
Count the number of ones in the binary representation of a given integer.

Input Format:
An integer.

Output Format:
An integer representing the count of ones in the binary representation of the input.

Sample Input:
9

Sample Output:
2
'''
numeroDecimal=int(input(""))
numeroHexadecimal=str(bin(numeroDecimal)).replace("0b","")
conta1=0
for i in numeroHexadecimal:
    if(i=='1'):
        conta1+=1
print(conta1)