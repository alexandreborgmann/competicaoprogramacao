class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def f(param):
            if param==1:
                return(1)
            else:
                produto = 1
                for i in range(1, param + 1 if param != n else param):
                    produto = max(produto, f(param-i)*i)
                return(produto)
        return(f(n))

objeto = Solution()
n = 2
n = 10
print(objeto.integerBreak(n))