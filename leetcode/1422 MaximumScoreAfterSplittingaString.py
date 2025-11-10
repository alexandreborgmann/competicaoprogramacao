class Solution:
    def maxScore(self, s: str) -> int:
        maior = 0
        for i in range(len(s)-1):
            zero = s[0:i+1].count('0')
            um = s[i+1:].count('1')
            #print('i=',i,zero,um,s[0:i+1],s[i+1:])
            if zero + um > maior:
                maior = zero + um
        return(maior)

objeto = Solution()
s = "011101"
#s = "00111"
#s = "1111"
print(objeto.maxScore(s))