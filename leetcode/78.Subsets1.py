from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        saida = [[]]
        for i in nums:
            saida += [lst + [i] for lst in saida]
            #print(saida,i)
        return saida

objeto = Solution()
nums = [1,2,3]
nums = [0]
nums = [1,2]
nums = [3,2,4,1]
print(objeto.subsets(nums))
