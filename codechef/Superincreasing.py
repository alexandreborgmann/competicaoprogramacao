t = int(input())
if t<1 or t>10**5:
    exit(1)
for i in range(t):
    n, k, x = map(int, input().split())
    arr = [0]*n
    arr[k-1] = x
    soma = 0
    errado = 0
    i = 0
    while i <= k-1 and errado == 0:
        if arr[i] == 0:
            arr[i] = soma+1
        else:
            if soma >= arr[i]:
                print('No')
                errado = 1
        soma += arr[i]
        i +=1
        #print(arr,soma,i)
    if errado == 0:
        print('Yes')