'''
Autor: Alexandre Borgmann
Data: 10/04/2020
URI Online Judge | 3065 Calculando

A disseminação dos computadores se deve principalmente à capacidade de eles se comportarem como outras máquinas, vindo a substituir muitas destas. Esta flexibilidade é possível porque podemos alterar a funcionalidade de um computador, de modo que ele opere da forma que desejarmos: essa é a base do que chamamos programação.
Sua tarefa é escrever um programa que faça com que o computador opere como uma calculadora simples. O seu programa deve ler expressões aritméticas e produzir como saída o valor dessas expressões, como uma calculadora faria. O programa deve implementar apenas um subconjunto reduzido das operações disponíveis em uma calculadora: somas e subtrações.

Entrada
A entrada é composta de vários conjuntos de testes. A primeira linha de um conjunto de testes contém um número inteiro m (1 ≤ m ≤ 100), indicando o número de operandos da expressão a ser avaliada. A segunda linha de um conjunto de testes contém a expressão aritmética a ser avaliada, no seguinte formato:
X1 s1 X2 s2 ... Xm-1 sm-1 Xm
onde
• Xi, 1 ≤ i ≤ m, é um operando (0 ≤ Xi ≤ 100);
• sj, 1 ≤ j < m, é um operador, representado pelos símbolos ‘+’ ou ‘–’;
• não há espaços em branco entre operandos e operadores. O final da entrada é indicado pelo valor m = 0.
Saída
Para cada conjunto de testes da entrada seu programa deve produzir três linhas. A primeira linha deve conter um identificador da expressão, no formato “Teste n”, onde n é numerado a partir de 1. Na segunda linha deve aparecer o resultado encontrado pelo seu programa. A terceira linha deve ser deixada em branco. A grafia mostrada no Exemplo de Saída, abaixo, deve ser seguida rigorosamente

Exemplo de Entrada
3
3+7-22
3
5-10-77
10
1+2+3+4+5+6+7+8+9+10
0
Exemplo de Saída
Teste 1
-12
Teste 2
-82
Teste 3
55
'''
contaTeste=1
while True:
    try:
        n = int(input(""))
    except:
        n=0
    if(n==0):
        break
    if(n<0 or n>100):
        print("0 ≤ Xi ≤ 100")
        continue
    expressao=input("")
    valor=""
    soma=0
    operador=1
    for i in expressao:
#        print("{} {} {} {}".format(i,valor,operador,soma))
        if(i.isdecimal()):
            valor+=i
        elif (i=='+'):
            soma+=(int(valor)*operador)
            valor=""
            operador=1
        elif(i=='-'):
            soma+=(int(valor)*operador)
            valor=""
            operador=-1
        else:
            operador=0
    soma += (int(valor) * operador)
    print("Teste {}".format(contaTeste))
    print(soma)
    print("")
    contaTeste+=1