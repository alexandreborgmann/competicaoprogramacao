from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i=0
        x = sorted(nums)
        while(x[i]<x[i+1]):
            i +=1
        return x[i]


objeto = Solution()
nums = [1,3,4,2,2]
#nums = [3,1,3,4,2]
#nums = [3,3,3,3,3]
print(objeto.findDuplicate(nums))

