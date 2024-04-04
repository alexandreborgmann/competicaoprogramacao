from typing import List
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        INF = 10 ** 20
        res = INF
        for l in range(N):
            produto = 0
            for r in range(l,N):
                produto |= nums[r]

                if produto >= k:
                    res = min(res, r - l + 1)
        if res == INF:
            return -1
        return res

objeto = Solution()
#nums = [1,2,3]
#k = 2
#nums = [2,1,8]
#k = 10
#nums = [1,2]
#k = 0
#nums = [16,1,2,20,32]
#k = 45
#nums = [32,2,24,1]
#k = 35
#nums = [32,1,25,11,2]
#k = 59
nums = [2,10,22,1,11,32]
k = 45
print(objeto.minimumSubarrayLength(nums, k))