from typing import List
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        soma = sum(nums)
        conta = len(nums)
        print(nums,k,soma,conta,'media=',soma/conta)

objeto = Solution()
nums = [2,5,6,8,5]
k = 4
nums = [2,5,6,8,5]
k = 7
nums = [1,2,3,4,5,6]
k = 4
print(objeto.minOperationsToMakeMedianK(nums, k))