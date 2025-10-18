'''
Autor: Alexandre Borgmann
Data: 11/04/2020
Sololearn Balconies

You are trying to determine which of two apartments has a larger balcony.
Both balconies are rectangles, and you have the length and width, but you need the area.

Task
Evaluate the area of two different balconies and determine which one is bigger.

Input Format
Your inputs are two strings where the measurements for height and width are separated by a comma. The first one represents apartment A, the second represents apartment B.

Output Format:
A string that says whether apartment A or apartment B has a larger balcony.

Sample Input
'5,5'
'2,10'

Sample Output
Apartment A
'''
linha = (input(""))
campos = linha.split(",")
apartamentoA=(int(campos[0])*int(campos[1]))
linha = (input(""))
campos = linha.split(",")
apartamentoB=(int(campos[0])*int(campos[1]))
if(apartamentoA>apartamentoB):
    print("Apartment A")
else:
    print("Apartment B")
