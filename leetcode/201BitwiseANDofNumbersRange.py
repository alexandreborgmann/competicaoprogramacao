class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0
        for i in range(32):
            bit = (left >> i) & 1
            if not bit:
                continue

            remain = left % (i << (i + 1))
            diff = (1 << (i + 1)) - remain
            if right - left < diff:
                res = res | (1 << i)

        return res

objeto = Solution()
left = 5
right = 7
left = 0
right = 0
left = 1
right = 2147483647
print(objeto.rangeBitwiseAnd(left, right))