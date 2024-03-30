from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        arr = [0 for _ in range(n)]

        for i in range(n):
            if 0< nums[i] <= n:
                arr[nums[i]-1] += 1
        print(nums,arr)
        for i in range(n):
            if arr[i] == 0:
                return(i+1)

objeto = Solution()
#nums = [1,2,0]
nums = [3,4,-1,1]
#nums = [7,8,9,11,12]
print(objeto.firstMissingPositive(nums))