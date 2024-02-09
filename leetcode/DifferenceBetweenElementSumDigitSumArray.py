from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        somad = 0
        for i in range(len(nums)):
            s = str(nums[i])
            for j in range(len(s)):
                somad += int(s[j])
        return(sum(nums)-somad)

objeto = Solution()
nums = [1, 15, 6, 3]
nums = [1,2,3,4]
print(objeto.differenceOfSum(nums))