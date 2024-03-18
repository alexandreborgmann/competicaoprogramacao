from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        maior = max(d.values())
        conta = 0
        for i in d.values():
            if i == maior:
                conta += i
        return conta

objeto = Solution()
nums = [1,2,2,3,1,4]
nums = [1,2,3,4,5]
print(objeto.maxFrequencyElements(nums))