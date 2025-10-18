from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return(nums[len(nums) - k])

objeto = Solution()
nums = [3,2,1,5,6,4]
k = 2
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(objeto.findKthLargest(nums, k))

