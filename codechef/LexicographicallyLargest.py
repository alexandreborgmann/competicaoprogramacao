def achaMaior(n, m, a):
    b = [m]*n
    GCD = m

    for i in range(n-1, -1, -1):
        if i == 0:
            b[i] = GCD
        else:
            potencial_gcd = GCD // a[i]
            b[i - 1] = potencial_gcd
            GCD = b[i-1] * a[i]
    return(b)

vezes = int(input(""))
if vezes > 10**4 and vezes < 1:
    exit(1)
for z in range(vezes):
    n, m = map(int, input("").split())
    a = list(map(int, input("").split()))

    r = achaMaior(n, m, a)
    print(*r)