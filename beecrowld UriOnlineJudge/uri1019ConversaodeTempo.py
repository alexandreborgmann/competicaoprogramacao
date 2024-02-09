'''
Author: Alexandre Borgmann
Date: 4/2/2020
URI Online Judge | 1019 Time Conversion

Read an integer value, which is the duration in seconds of a given event in a factory, and enter it expressed in the format hours: minutes: seconds.
Input
The input file contains an integer value N.
Output
Print the time read in the input file (seconds), converted to hours: minutes: seconds, according to the example provided.

Input Example / Output Example
556
0:9:16
1
0:0:1
140153
38:55:53
'''

segundos = int(input())
horas = segundos // 3600
segundosRestantes = segundos % 3600
minutos = segundosRestantes // 60
segundos = segundosRestantes % 60

print('{}:{}:{}'.format(horas,minutos,segundos))
