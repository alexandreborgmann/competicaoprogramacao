'''
Autor: Alexandre Borgmann
Data: 11/04/2020
Sololearn Vowel Counter

You are in an English class, your teacher tells the class that vowels are the glue that hold words and sentences together.
They want to make sure you understand the importance of vowels in a sentence.
You are given example sentences and are to give a total amount of vowels that are in each sentence.

Task:
Write a program that takes in a string as input, counts and outputs the number of vowels (A, E, I, O, U).

Input Format:
A string (letters can be both uppercase or lower case).

Output Format:
A number which represents the total number of vowels in the string.

Sample Input:
this is a sentence

Sample Output:
6
'''
numeroVogais=0
frase= input("")
for i in frase:
    if(i.upper() in ('A','E','I','O','U')):
        numeroVogais+=1
print(numeroVogais)
