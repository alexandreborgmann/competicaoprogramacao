class Solution:
    def integerBreak(self, n: int) -> int:
        def f(param):
            if param==1:
                return(1)
            else:
                resposta = 1*(param-1)
                i = 1
                while i<param:
                    primeiro = i
                    segundo = param - i
                    produto = primeiro * (max(segundo, f(segundo)))
                    if produto > resposta:
                        resposta = produto
                    i += 1
                    #print(primeiro, segundo, produto, i, resposta)
                return resposta
        return f(n)

objeto = Solution()
n = 2
n = 10
print(objeto.integerBreak(n))