from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        s = [[]]
        for i in range(len(nums)):
            x = []
            x.append(nums[i])
            s.append(x)
            for j in range(i+1, len(nums)):
                x = []
                x.append(nums[i])
                x.append(nums[j])
                if x not in s:
                    s.append(x)
        if len(nums) > 1 and nums not in s:
            s.append(nums)
        return s

objeto = Solution()
nums = [1,2,3]
nums = [0]
nums = [1,2]
nums = [3,2,4,1]
print(objeto.subsets(nums))
