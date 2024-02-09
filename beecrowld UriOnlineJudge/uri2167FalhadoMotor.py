'''
Author: Alexandre Borgmann
Date: 5/4/2020
URI Online Judge | 2167 Falha do Motor

Ao observar a curva de velocidade de um motor, o engenheiro Zé percebeu que sempre ocorria uma queda quando as medidas eram feitas em
intervalos de 10 ms.
Mas esta queda acontecia em medidas diferentes a cada novo teste do motor.
Zé ficou curioso com essa falta de padrão e quer saber, para cada teste do motor, qual a primeira medida em que ocorre uma queda de velocidade.
Entrada
A entrada é um teste do motor e é dada em duas linhas.
A primeira tem o número N de medidas de velocidade do motor (1 < N ≤ 100).
A segunda linha tem N inteiros: o número de RPM (rotações por minuto) Ri de cada medida (0 ≤ Ri ≤ 10000, para todo Ri, tal que 1 ≤ i ≤ N).
Uma medida é considerada uma queda se é menor que a medida anterior.
Saída
A saída é o índice da medida em que houve a primeira queda de velocidade no teste.
Caso não aconteça uma queda de velocidade a saída deve ser o número zero.

Exemplos de Entrada
3
1 4 2
5
100 199 199 198 0
Exemplos de Saída
3
4
'''
while True:
    leitura = int(input(""))
    if(leitura<=1 or leitura>100):
        print("Deve ser (1 < N ≤ 100)")
        continue
    break
linha = input("")
campos = linha.split()
achou=0
MedidaVelocidade = []
for i in range(leitura):
    MedidaVelocidade.append(int(campos[i]))
for i in range(leitura):
    if(MedidaVelocidade[i]<MedidaVelocidade[i-1] and i>0):
        achou=1
        print(i+1)
        break
if(achou==0):
    print(0)