'''
Autor: Alexandre Borgmann
Data: 11/04/2020
Sololearn Data Science - Average of Rows +50 XP

In a matrix, or 2-d array X, the averages (or means) of the elements of rows is called row means.

Task
Given a 2D array, return the rowmeans.

Input Format
First line: two integers separated by spaces, the first indicates the rows of matrix X (n) and the second indicates the columns of X (p)
Next n lines: values of the row in X

Output Format
An numpy 1d array of values rounded to the second decimal.

2 2
1.5 1
2 2.9

Sample Output
[1.25 2.45]

'''
import numpy as np
matriz = []

linha=input("")
campos=linha.split()
x=int(campos[0])
y=int(campos[1])
for i in range(x):
    linha = input("")
    campos=linha.split()
    matriz.append(campos)

arr = np.array(matriz).astype(float)
arr = np.around(arr, decimals=2)
arr = arr.reshape(x,y)
print(arr.mean(axis=1))
