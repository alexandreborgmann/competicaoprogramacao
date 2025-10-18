from typing import List
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if max(nums) > k:
            return 1
        else:
            menor = -1
            conta = 1
            produto = nums[0]
            for i in range(1,len(nums)):
                if nums[i-1] | nums[i] > k:
                    return 2
                produto = produto | nums[i]
                print('i=',i, nums[i], 'produto=',produto, produto | nums[i], nums[i-1]|nums[i],'menor=',menor,'conta=',conta)
                if produto >= k:
                    if menor == -1 or conta < menor:
                        menor = conta+1
                        conta = 1
                        produto = nums[i]
                else:
                    conta += 1
        return menor

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