'''
Autor: Alexandre Borgmann
Data: 08/04/2020
URI Online Judge | 2756 Saída 10

O seu professor de programação gostaria que você fizesse um programa com as seguintes características:
Coloque sete espaços em branco e coloque o carácter 'A';
Coloque seis espaços em branco e coloque o carácter 'B', um espaço em branco e o carácter 'B';
Coloque cinco espaços em branco e coloque o carácter 'C', três espaço em branco e o carácter 'C';
Coloque quatro espaços em branco e coloque o carácter 'D', cinco espaço em branco e o carácter 'D';
Coloque três espaços em branco e coloque o carácter 'E', sete espaço em branco e o carácter 'E';
Repita o procedimento 4;
Repita o procedimento 3;
Repita o procedimento 2;
Repita o procedimento 1.
Entrada
Não há.
Saída
O resultado de seu programa deve ser escrito conforme o exemplo de saída.

Exemplo de Entrada
Exemplo de Saída

       A
      B B
     C   C
    D     D
   E       E
    D     D
     C   C
      B B
       A
'''
print(" "*7+"A")
print(" "*6+"B"+" "*1+"B")
print(" "*5+"C"+" "*3+"C")
print(" "*4+"D"+" "*5+"D")
print(" "*3+"E"+" "*7+"E")
print(" "*4+"D"+" "*5+"D")
print(" "*5+"C"+" "*3+"C")
print(" "*6+"B"+" "*1+"B")
print(" "*7+"A")