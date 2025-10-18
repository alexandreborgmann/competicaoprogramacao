num = int(input(""))
if num>46:
    exit(1)

n1 = 0
n2 = 1
Sum = 0
i = 0

while (i < num):
    print(n1,end='')
    Sum = Sum + n1
    Next = n1 + n2
    n1 = n2
    n2 = Next
    i = i + 1
    if i < num:
        print(' ',end='')
print('')

