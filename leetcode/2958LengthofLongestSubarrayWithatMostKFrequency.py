from typing import List
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dic = {}
        resultado = []
        for i in range(len(nums)):
            if nums[i] in dic:
                if dic[nums[i]]<k:
                    dic[nums[i]] +=1
                    resultado.append(nums[i])
            else:
                dic[nums[i]] = 1
                resultado.append(nums[i])
        print(dic,resultado)
        return(len(resultado))

objeto = Solution()
#nums = [1,2,3,1,2,3,1,2]
#k = 2
#nums = [1,2,1,2,1,2,1,2]
#k = 1
#nums = [5,5,5,5,5,5,5]
#k = 4
nums = [1,4,4,3]
k = 1
print(objeto.maxSubarrayLength(nums, k))