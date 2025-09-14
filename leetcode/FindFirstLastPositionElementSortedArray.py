from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lista = [-1, -1]
        i = 0
        while True:
            try:
                i = nums.index(target, i)
            except:
                break
            if lista[0]==-1:
                lista[0] = i
            lista[1] = i
            i += 1
        return lista

objeto = Solution()
'''
nums = [5,7,7,8,8,10]
target = 8
nums = [5,7,7,8,8,10]
target = 6
'''
nums = []
target = 0
print(objeto.searchRange(nums, target))