from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsSet = set(nums)
        tamanho = len(nums) / 2
        for i in numsSet:
            if nums.count(i) >= tamanho:
                return i

objeto = Solution()
nums = [3,2,3]
#nums = [2,2,1,1,1,2,2]
print(objeto.majorityElement(nums))