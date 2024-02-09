from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        tamanho = len(nums)
        nums = sorted(set(nums))
        resultado = tamanho
        j = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j]< nums[i] + tamanho:
                j += 1
            janela = j - i
            resultado = min(resultado, tamanho - janela)

        return(resultado)

objeto = Solution()
#nums = [4,2,5,3]
#nums = [1,2,3,5,6]
nums = [1,10,100,1000]
print(objeto.minOperations(nums))