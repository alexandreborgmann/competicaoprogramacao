from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maior = max(nums)
        n=nums.count(maior)
        if n < k:
            return 0
        r = 0
        for i in range(len(nums)):
            conta = 0
            j = i
            while j < len(nums):
                if nums[j] == maior:
                    conta += 1
                if conta == k:
                    r += len(nums)-j
                    break
                j += 1
                print(i,j,r,nums[i:j])
        return r

objeto = Solution()
nums = [1,3,2,3,3]
k = 2
#nums = [1,4,2,1]
#k = 3
print(objeto.countSubarrays(nums, k))