from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resposta = []

        for i in range(len(nums)):
            if i>0:
                inicio = nums[0:i]
            else:
                inicio = []
            if i < len(nums)-1:
                fim = nums[i+1:]
            else:
                fim = []
            todos = inicio + fim
            produto = 1
            for i in todos:
                produto *=i
            resposta.append(produto)
        return resposta

objeto = Solution()
nums = [1,2,3,4]
#nums = [-1,1,0,-3,3]
print(objeto.productExceptSelf(nums))