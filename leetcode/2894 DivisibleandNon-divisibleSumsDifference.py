class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for i in range(1,n+1):
            if i%m != 0:
                num1 += i
            if i%m == 0:
                num2 += i
        return(num1 - num2)

objeto = Solution()
'''
n = 10
m = 3
n = 5
m = 6
'''
n = 5
m = 1
print(objeto.differenceOfSums(n, m))