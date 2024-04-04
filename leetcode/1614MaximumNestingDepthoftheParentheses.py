class Solution:
    def maxDepth(self, s: str) -> int:
        soma = 0
        maior = 0
        for i in range(len(s)):
            if s[i]=='(':
                soma += 1
                maior = max(maior, soma)
            if s[i]==')':
                soma -= 1
        return maior

objeto = Solution()
s = "(1+(2*3)+((8)/4))+1"
#s = "(1)+((2))+(((3)))"
print(objeto.maxDepth(s))