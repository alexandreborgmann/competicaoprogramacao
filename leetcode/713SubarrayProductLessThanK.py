from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        product = 1
        for r in range(len(nums)):
            product *= nums[r]

            if product >= k:
                while product >= k and l <= r:
                    product /= nums[l]
                    l += 1
            res += r - l + 1
            #print('fora product=',product,'res=',res,'l=',l,'r',r)
        return res

objeto = Solution()
nums = [10,5,2,6]
k = 100
#nums = [1,2,3]
#k = 0
print(objeto.numSubarrayProductLessThanK(nums, k))