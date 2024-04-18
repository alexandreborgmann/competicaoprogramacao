from typing import List
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def primo(n, i=2):
            if n <= 2:
                return n == 2
            if n % i == 0:
                return False
            if i * i > n:
                return True
            return primo(n, i + 1)
        menor=-1
        maior=-1
        for i in range(len(nums)):
            if primo(nums[i]):
                if menor==-1 or i<menor:
                    menor = i
                if i > maior:
                    maior = i
        #print(menor, maior)
        return(maior-menor)

        pass

objeto = Solution()
nums = [4,2,9,5,3]
#nums = [4,8,2,8]
print(objeto.maximumPrimeDifference(nums))