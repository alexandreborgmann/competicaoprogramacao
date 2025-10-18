def fatorial(n):
    if n==0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

t = int(input())
for i in range(t):
    i = int(input(""))
    print(fatorial(i))