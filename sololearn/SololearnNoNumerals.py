'''
Autor: Alexandre Borgmann
Data: 11/04/2020
Sololearn No Numerals

You write a phrase and include a lot of number characters (0-9), but you decide that for numbers 10 and under you would rather
write the word out instead.
Can you go in and edit your phrase to write out the name of each number instead of using the numeral?

Task:
Take a phrase and replace any instances of an integer from 0-10 and replace it with the English word that corresponds to that integer.

Input Format:
A string of the phrase in its original form (lowercase).

Output Format:
A string of the updated phrase that has changed the numerals to words.

Sample Input:
i need 2 pumpkins and 3 apples

Sample Output:
i need two pumpkins and three apples
'''
numeroExtenso = { 0 : "zero", 1 : "one", 2: "two", 3: "three", 4 : "four", 5 : "five", 6 : "six",
                  7: "seven", 8 : "eight", 9 : "nine", 10: "ten"}
frase = input("").split()
for i in frase:
    if(i.isdigit()):
        if(int(i)>=0 and int(i)<=10):
            print(numeroExtenso[int(i)],end=" ")
            continue
    print(i,end=" ")
print("")
