from typing import List
from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            while count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1

            res = max(res,(r - l + 1))
        return res
objeto = Solution()
#nums = [1,2,3,1,2,3,1,2]
#k = 2
#nums = [1,2,1,2,1,2,1,2]
#k = 1
#nums = [5,5,5,5,5,5,5]
#k = 4
nums = [1,4,4,3]
k = 1
print(objeto.maxSubarrayLength(nums, k))