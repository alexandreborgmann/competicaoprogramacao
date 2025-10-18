class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            i +=1
        return left << i

objeto = Solution()
left = 5
right = 7
#left = 0
#right = 0
#left = 1
#right = 2147483647
print(objeto.rangeBitwiseAnd(left, right))