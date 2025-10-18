vezes = int(input(""))
for i in range(vezes):
    num = int(input(""))

    n1 = 0
    n2 = 1
    Sum = 0
    i = 0

    while (i < num):
        Sum = Sum + n1
        Next = n1 + n2
        n1 = n2
        n2 = Next
        i = i + 1
    print('Fib({}) = {}'.format(num,n1))