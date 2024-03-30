from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        resultado = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                resultado.append(nums[i])
        return(resultado)

objeto = Solution()
nums = [4,3,2,7,8,2,3,1]
nums = [1,1,2]
nums = [1]
print(objeto.findDuplicates(nums))