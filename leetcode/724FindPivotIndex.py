from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            somaEsquerda = 0
            for j in range(0, i):
                somaEsquerda += nums[j]
            somaDireita = 0
            for j in range(i+1,len(nums)):
                somaDireita +=nums[j]
                #print('j=', j, somaDireita, nums[j])
            if somaEsquerda == somaDireita:
                return i
            #print(i,somaEsquerda,somaDireita)
        return -1

objeto = Solution()
nums = [1,7,3,6,5,6]
#nums = [1,2,3]
#nums = [2,1,-1]
print(objeto.pivotIndex(nums))