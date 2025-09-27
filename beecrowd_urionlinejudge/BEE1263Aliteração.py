'''
beecrowd | 1263
Aliteração
Por TopCoder*  EUA

Timelimit: 1
Uma aliteração ocorre quando duas ou mais palavras consecutivas de um texto possuem a mesma letra inicial (ignorando maiúsculas e minúsculas). Sua tarefa é desenvolver um programa que identifique, a partir de uma sequência de palavras, o número de aliterações que essa sequência possui.

Entrada
A entrada contém diversos casos de testes. Cada caso é expresso como um texto em uma única linha, contendo de 1 a 100 palavras separadas por um único espaço, cada palavra tendo de 1 a 50 letras minúsculas ou maiúsculas ('A'-'Z','a'-'z'). A entrada termina em EOF.

Saída
Para cada caso de teste imprima o número de aliterações existentes no texto informado, conforme exemplos abaixo.
'''
while True:
    try:
        linha = input().upper()
        if linha == "":
            break
        lista = list(map(str, linha.split()))
        conta_total = 0
        conta = 0
        letra_anterior = ''
        for i in range(len(lista)):
#            print('inicio= ',lista[i], letra_anterior, lista[i][0], lista, conta, conta_total)
            if letra_anterior == lista[i][0]:
                conta += 1
            else:
                letra_anterior = lista[i][0]
                if conta >= 1:
                    conta_total += 1
                conta = 0
#            print('fim= ',lista[i],letra_anterior, lista[i][0], lista, conta, conta_total)
        if conta >= 1:
            conta_total += 1
        print(conta_total)
    except (EOFError, ValueError):
        break
