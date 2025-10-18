from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unico = set(nums1)

        resultado = []
        for n in nums2:
            if n in unico:
                resultado.append(n)
                unico.remove(n)
        return resultado


objeto = Solution()
#nums1 = [1,2,2,1]
#nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(objeto.intersection(nums1, nums2))