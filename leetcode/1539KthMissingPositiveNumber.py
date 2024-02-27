from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        numero = 0
        i = 0
        while k > 0 and i < len(arr):
            numero += 1
            #print('numero',numero,'k',k,'i',i,'arr[i]',arr[i])
            if numero != arr[i]:
                k -= 1
            else:
                i += 1

        if k > 0:
            #print('fim if', 'numero', numero, 'k', k)
            return arr[-1]+k
        else:
            #print('fim else','numero',numero,'k',k)
            return(numero)

objeto = Solution()
arr = [2,3,4,7,11]
k = 5
#arr = [1,2,3,4]
#k = 2
print(objeto.findKthPositive(arr, k))