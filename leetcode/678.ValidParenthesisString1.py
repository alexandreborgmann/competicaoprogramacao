class Solution:
    def checkValidString(self, s: str) -> bool:
        esquerdoMin, esquerdoMax = 0, 0
        for c in s:
            if c == '(':
                esquerdoMin += 1
                esquerdoMax += 1
            elif c == ')':
                esquerdoMin -= 1
                esquerdoMax -= 1
            else:
                esquerdoMin -= 1
                esquerdoMax += 1
            if esquerdoMax < 0:
                return False
            if esquerdoMin < 0:
                esquerdoMin = 0
        return esquerdoMin == 0
objeto = Solution()
#s = "()"
#s = "(*)"
#s = "(*))"
s = "((((((()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
print(objeto.checkValidString(s))