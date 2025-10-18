pulo, vezes = map(int, input().split())
canos = list(map(int, input().split()))
for i in range(vezes-1):
    if abs(canos[i]-canos[i+1])>pulo:
        print('GAME OVER')
        exit(0)
print('YOU WIN')
