class Solution:
    def isNumber(self, s: str) -> bool:
        if s.upper().find('INF') != -1 or s.upper().find('NAN') != -1:
            return(False)
        try:
            i = float(s)
        except:
            return(False)
        return(True)

objeto = Solution()
s = "0"
s = "e"
#s = "."
s = "inf"
print(objeto.isNumber(s))

