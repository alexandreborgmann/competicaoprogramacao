from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {}

        def dfs(i):
            if i == len(nums):
                return []
            if i in cache:
                return cache[i]

            res = [nums[i]]
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + dfs(j)
                    if len(tmp) > len(res):
                        res = tmp
            cache[i] = res
            #print('dfs res',res,'i',i)
            return res

        res = []
        for i in range(len(nums)):
            #print('i=',i)
            tmp = dfs(i)
            if len(tmp) > len(res):
                res = tmp
        return res


objeto = Solution()
nums = [1,2,3]
#nums = [1,2,4,8]
print(objeto.largestDivisibleSubset(nums))