'''
Autor: Alexandre Borgmann
Data: 19/04/2020
Sololearn Average Word Length

You are in a college level English class, your professor wants you to write an essay, but you need to find out the average length
of all the words you use. It is up to you to figure out how long each word is and to average it out.

Task:
Takes in a string, figure out the average length of all the words and return a number representing the average length.
Remove all punctuation. Round up to the nearest whole number.

Input Format:
A string containing multiple words.

Output Format:
A number representing the average length of each word, rounded up to the nearest whole number.

Sample Input:
this phrase has multiple words

Sample Output:
6
'''
import math

linha = input("").split(" ")
conta = 0
tamanho = 0
for i in linha:
    conta+=1
    tamanho+=len(i.translate({ord(c):'' for c in "!?.,:;><="}))
#    print(len(i),' ',conta,' ',i,' ',tamanho)
print(math.ceil(tamanho/conta))

