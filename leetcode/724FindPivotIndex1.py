from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        global_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if global_sum - (2 * left_sum) == num:
                return i
            left_sum += num
        return -1

objeto = Solution()
nums = [1,7,3,6,5,6]
#nums = [1,2,3]
#nums = [2,1,-1]
print(objeto.pivotIndex(nums))