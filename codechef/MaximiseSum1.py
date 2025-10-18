from numba import jit, njit
from typing import List

@jit(nopython=True)
def soma(n: int, a: List[int]):
    for l in range(n):
        for r in range(l,n):
            for i in range(l+1,r):
                #if i>l and i<r:
                if a[i]<min(a[l],a[r]):
                    a[i] = min(a[l],a[r])
                    #print('troquei ',a[i],min(a[l],a[r]))
                #print('i=',i,'l=',l,'r',r,a[l],a[r])
    print(sum(a))

vezes = int(input(""))
if vezes > 10**5 and vezes < 1:
    exit(1)
for z in range(vezes):
    n = int(input(""))
    a = list(map(int, input("").split()))
    soma(n, a)

