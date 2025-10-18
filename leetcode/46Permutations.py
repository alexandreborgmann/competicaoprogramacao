from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        resultado = []
        resultado.append(nums)
        numsaux = []
        for i in range(N):
            for j in range(N):
                numsaux = nums.copy()
                print('inicio ',numsaux)
                if i != j:
                    aux = numsaux[i]
                    numsaux[i] = numsaux[j]
                    numsaux[j] = aux
                    if numsaux not in resultado:
                        resultado.append(numsaux)
                print(i,j,nums, 'numsaux=',numsaux, resultado)
        return(resultado)

objeto = Solution()
nums = [1,2,3]
#nums = [0,1]
#nums = [1]
print(objeto.permute(nums))