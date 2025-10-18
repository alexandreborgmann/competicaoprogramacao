t = int(input())
if t<1 or t>1000:
    exit(1)
for z in range(t):
    n, k = map(int, input("").split())
    a = list(map(int, input("").split()))
    total = sum(a)
    one = False

    if (total >= n and k > 0):
        one = True
    elif (total >= n and k == 0):
        if (total % n == 0):
            one = True

    if(one):
        print('YES')
    else:
        print('NO')
'''
    total = sum(a)
    #print(sum(a), (k*n))
    if total < n and k>0:
        print('NO')
    elif sum(a)<=(k*n)+n:
        print('YES')
    else:
        print('NO')
'''



'''

def can_redistribute_chocolates(N, K, A):
    A.sort()  # Sort the array in ascending order
    min_chocolates = min(A)  # Minimum chocolates any child has

    # Calculate the maximum chocolates a child can have
    max_chocolates = min_chocolates + K

    # Check if each child can have chocolates in the desired range
    for i in range(N):
        if A[i] < max_chocolates:
            A[i] = max_chocolates
        else:
            break

    # Check if the redistribution is successful for all children
    return all(choco >= min_chocolates and choco <= max_chocolates for choco in A)
'''