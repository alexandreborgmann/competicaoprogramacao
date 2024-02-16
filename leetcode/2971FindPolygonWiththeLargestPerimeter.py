from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = -1
        total = 0

        for n in nums:
            if total > n:
                res = max(res, total + n)
            total += n
        return res


objeto = Solution()
#nums = [5,5,5]
#nums = [1,12,1,2,5,50,3]
nums = [5,5,50]
print(objeto.largestPerimeter(nums))