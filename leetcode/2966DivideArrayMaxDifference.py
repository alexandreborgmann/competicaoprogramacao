from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return([])
            res.append(nums[i:i+3])
        return(res)

nums = [1,3,4,8,7,9,3,5,1]
k = 2
objeto = Solution()
print(objeto.divideArray(nums, k))

