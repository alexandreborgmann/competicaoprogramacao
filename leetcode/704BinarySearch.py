from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = int((l + r) / 2)
            #print(l, r, m, nums[l:r+1])
            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1

objeto = Solution()
nums = [-1,0,3,5,9,12]
target = 9
#nums = [-1,0,3,5,9,12]
#target = 2
print(objeto.search(nums, target))