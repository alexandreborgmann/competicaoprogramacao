'''
Autor: Alexandre Borgmann
Data: 11/04/2020
Sololearn Data Science - Reshape

Task
Given a list of numbers and the number of rows (r), reshape the list into a 2-dimensional array. 
Note that r divides the length of the list evenly.

Input Format
First line: an integer (r) indicating the number of rows of the 2-dimensional array
Next line: numbers separated by the space
 
Output Format
An numpy 2d array of values rounded to the second decimal.

Sample Input
2
1.2 0 0.5 -1

Sample Output
[[ 1.2  0. ]
 [ 0.5 -1. ]]
'''
import numpy as np

nroLinha = int(input(""))
#lst = [float(x) for x in input().split()]
linha = input("")
vetor=linha.split()

arr = np.array(vetor).astype(float)
arr = np.around(arr, decimals=2)
arr = arr.reshape(nroLinha,2)
print(arr)
