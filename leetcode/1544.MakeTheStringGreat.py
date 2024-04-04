class Solution:
    def makeGood(self, s: str) -> str:
        removeu = True
        while removeu:
            removeu = False
            i = 0
            while i < len(s)-1:
                #print(i, s[i], s[i + 1], s)
                if s[i].upper() == s[i+1].upper() and s[i] != s[i+1]:
                    s = "".join(s[0:i])+"".join(s[i+2:])
                    removeu = True
                else:
                    i += 1
        return s

objeto = Solution()
s = "leEeetcode"
#s = "abBAcC"
#s = "s"
print(objeto.makeGood(s))