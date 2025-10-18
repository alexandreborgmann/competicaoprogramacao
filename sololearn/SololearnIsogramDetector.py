'''
Autor: Alexandre Borgmann
Data: 10/04/2020
Sololearn Isogram Detector

An isogram is a word that has no repeating letters, whether they are consecutive or non-consecutive.
Your job is to find a way to detect if a word is an isogram.

Task: Write a program that takes in a string as input, detects if the string is an isogram and outputs true or false based on the result.

Input Format:
A string containing one word.

Output Format:
A string: true or false.

Sample Input:
turbulence

Sample Output:
false

Um isograma é uma palavra que não possui letras repetidas, sejam consecutivas ou não consecutivas.
Seu trabalho é encontrar uma maneira de detectar se uma palavra é um isograma.

Tarefa: Escreva um programa que receba uma sequência como entrada, detecte se a sequência é um isograma e gera verdadeiro ou falso com base no resultado.

Formato de entrada:
Uma sequência contendo uma palavra.

Formato de saída:
Uma sequência: verdadeira ou falsa.

Entrada de amostra:
turbulência

Saída de amostra:
false
'''
contai=0
achou=0
entrada=input("")
for i in entrada:
    contaj = 0
    for j  in entrada:
        if(i==j and contai!=contaj):
            print("false")
            exit(0)
        contaj+=1
    contai+=1
print("true")