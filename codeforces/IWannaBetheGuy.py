nivelJogo = int(input(""))
x = list(map(int, input("").split()))
y = list(map(int, input("").split()))
x.pop(0)
y.pop(0)
ambos = set(x+y)
for i in range(1,nivelJogo+1):
    if i not in ambos:
        print('Oh, my keyboard!')
        exit(0)
print('I become the guy.')
