from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x):
            if x < 0:
                return 0
            res = 0
            l, cur = 0, 0
            for r in range(len(nums)):
                cur += nums[r]
                while cur > x:
                    cur -= nums[l]
                    l += 1
                res += (r - l + 1)
            return res

        return helper(goal) - helper(goal - 1)

objeto = Solution()
nums = [1,0,1,0,1]
goal = 2
#nums = [0,0,0,0,0]
#goal = 0
print(objeto.numSubarraysWithSum(nums, goal))