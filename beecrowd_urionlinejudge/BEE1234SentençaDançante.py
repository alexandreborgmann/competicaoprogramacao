'''
beecrowd | 1234
Sentença Dançante
Por TopCoder*  EUA

Timelimit: 1
Uma sentença é chamada de dançante se sua primeira letra for maiúscula e cada letra subsequente for o oposto da letra anterior. Espaços devem ser ignorados ao determinar o case (minúsculo/maiúsculo) de uma letra. Por exemplo, "A b Cd" é uma sentença dançante porque a primeira letra ('A') é maiúscula, a próxima letra ('b') é minúscula, a próxima letra ('C') é maiúscula, e a próxima letra ('d') é minúscula.

Entrada
A entrada contém vários casos de teste. Cada caso de teste é composto por uma linha que contém uma sentença, que é uma string que contém entre 1 e 50 caracteres ('A'-'Z','a'-'z' ou espaço ' '), inclusive, ou no mínimo uma letra ('A'-'Z','a'-'z').

Saída
Transforme a sentença de entrada em uma sentença dançante (conforme o exemplo abaixo) trocando as letras para minúscula ou maiúscula onde for necessário. Todos os espaços da sentença original deverão ser preservados, ou seja, " sentence " deverá ser convertido para " SeNtEnCe ".
'''
while True:
    try:
        linha = input()

        resultado = []
        maiuscula = True

        for char in linha:
            if char == ' ':
                resultado.append(char)
                continue

            # Se não for letra, adiciona sem alterar e não alterna
            if not char.isalpha():
                resultado.append(char)
                continue

            if maiuscula:
                resultado.append(char.upper())
            else:
                resultado.append(char.lower())

            maiuscula = not maiuscula

        print(''.join(resultado))

    except EOFError:
        break