from typing import List
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()

        meio = len(nums) // 2
        troca = 0
        if nums[meio] > k:
            troca += abs(k - nums[meio])
            nums[meio] = k
            i = meio - 1
            while i >= 0 and nums[i] > nums[meio]:
                troca += abs(nums[i] - nums[meio])
                i -= 1
        else:
            troca += abs(k - nums[meio])
            nums[meio] = k
            i = meio + 1
            while i < len(nums) and nums[i] < nums[meio]:
                troca += abs(nums[i] - nums[meio])
                i += 1
        return troca

objeto = Solution()
nums = [2,5,6,8,5]
k = 4
nums = [2,5,6,8,5]
k = 7
nums = [1,2,3,4,5,6]
k = 4
print(objeto.minOperationsToMakeMedianK(nums, k))