'''
Autor: Alexandre Borgmann
Data: 08/04/2020
URI Online Judge | 2752 Saída 6

O seu professor de programação gostaria que você fizesse um programa com as seguintes características:
Crie uma variável para armazenar 50 caracteres;
Atribua a variável anterior a frase: "AMO FAZER EXERCICIO NO URI";
Mostre na primeira linha o carácter <, o valor armazenado na variável com o formato "%s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%30s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%.20s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%-20s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%-30s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%.30s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%30.20s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%-30.20s" e o carácter >;
Entrada
Não há.
Saída
O resultado de seu programa deve ser escrito conforme o exemplo da saída.

Exemplo de Entrada
Exemplo de Saída
<AMO FAZER EXERCICIO NO URI>
<    AMO FAZER EXERCICIO NO URI>
<AMO FAZER EXERCICIO >
<AMO FAZER EXERCICIO NO URI>
<AMO FAZER EXERCICIO NO URI    >
<AMO FAZER EXERCICIO NO URI>
<          AMO FAZER EXERCICIO >
<AMO FAZER EXERCICIO           >
'''
vetor="AMO FAZER EXERCICIO NO URI"
print("<{}>".format(vetor))        #"%s" <AMO FAZER EXERCICIO NO URI>
print("<{:>30}>".format(vetor))     #"%30s" <    AMO FAZER EXERCICIO NO URI>
print("<{}>".format(vetor[0:20]))     #"%.20s" <AMO FAZER EXERCICIO >
print("<{:20}>".format(vetor))     #"%-20s" <AMO FAZER EXERCICIO NO URI>
print("<{:<30}>".format(vetor))     #"%-30s" <AMO FAZER EXERCICIO NO URI    >
print("<{}>".format(vetor[0:30]))     #"%.30s" <AMO FAZER EXERCICIO NO URI>
print("<{:>30}>".format(vetor[0:20]))     #"%30.20s" <          AMO FAZER EXERCICIO >
print("<{:<30}>".format(vetor[0:20]))     #"%-30.20s" <AMO FAZER EXERCICIO           >

