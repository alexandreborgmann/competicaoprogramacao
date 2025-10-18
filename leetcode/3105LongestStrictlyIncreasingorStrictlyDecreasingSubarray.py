from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        maior = 0
        # crescente
        while r < len(nums)-1:
            if nums[r] >= nums[r+1]:
                #print('dentro ',l,r)
                maior = max(maior, (r-l)+1)
                l = r+1
            #print(f'crescente l={l} r={r} maior={maior} nums[r]={nums[r]} nums[r+1]={nums[r+1]}')
            r += 1
        maior = max(maior,r-l+1)
        l = 0
        r = 0
        while r < len(nums)-1:
            if nums[r] <= nums[r+1]:
                #print('dentro ', l, r)
                maior = max(maior, (r-l)+1)
                l = r+1
            #print(f'decrescente l={l} r={r} maior={maior} nums[r]={nums[r]} nums[r+1]={nums[r+1]}')
            r += 1
        maior = max(maior,r-l+1)
        if maior == 0:
            return 1

        return maior

objeto = Solution()
nums = [1,4,3,3,2]
#nums = [3,3,3,3]
#nums = [3, 2, 1]
#nums = [1,1,5]
print(objeto.longestMonotonicSubarray(nums))