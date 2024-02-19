class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while 2 ** i <= n:
            if 2 ** i == n:
                return True
            i += 1
        return False

n = 1
#n = 16
#n =3

objeto = Solution()
print(objeto.isPowerOfTwo(n))