import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and math.log(n,4) % 1 == 0

        '''
        if n == 1:
            return True
        if n <= 0 or n % 4:
            return False
        return self.isPowerOfFour(n // 4)

        for i in range(n):
            if n == 4**i:
                return(True)
        return False
        '''
objeto = Solution()
n = 16
n = 5
#n = 1
print(objeto.isPowerOfFour(n))
