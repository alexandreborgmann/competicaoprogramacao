from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        resposta = []
        i = 0
        tam = len(nums) / 3
        while i<len(nums):
            #print('count=',nums.count(nums[i]),'i=',i,'nums[i]=',nums[i],'nums=',nums)
            conta = nums.count(nums[i])
            if conta > tam:
                resposta.append(nums[i])
                while conta>1:
                    nums.remove(resposta[-1])
                    conta -= 1
                    #print(resposta[-1],conta)
            i += 1
            #print(tam,resposta)
        return(resposta)

objeto = Solution()
nums = [3, 2, 3]
#nums = [1]
#nums = [1,2]
#nums = [2,2]
nums = [1,2,1,2,3]
print(objeto.majorityElement(nums))