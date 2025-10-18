class Solution:
    def scoreOfString(self, s: str) -> int:
        soma = 0
        for i in range(len(s)-1):
            soma += abs(ord(s[i])-ord(s[i+1]))
            #print(s[i], ord(s[i]), s[i+1], ord(s[i+1]), soma,)
        return soma

objeto = Solution()
s = "hello"
#s = "zaz"
print(objeto.scoreOfString(s))