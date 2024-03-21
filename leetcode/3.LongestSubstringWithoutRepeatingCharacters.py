class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        frase = ""
        maior = 1
        for i in s:
            if i not in frase:
                frase +=i
            else:
                frase = frase[frase.find(i)+1:]
                frase += i
            maior = max(maior, len(frase))
            #print(i,frase,maior)
        maior = max(maior, len(frase))
        return(maior)

objeto = Solution()
s = "abcabcbb"
#s = "bbbbb"
#s = "pwwkew"
#s = " "
#s = "au"
#s = "dvdf"
print(objeto.lengthOfLongestSubstring((s)))