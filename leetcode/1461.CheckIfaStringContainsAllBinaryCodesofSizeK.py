class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codeSet = set()
        for i in range(len(s) - k + 1):
            codeSet.add(s[i: i + k])
        return len(codeSet) ==  2 ** k

objeto = Solution()
s = "00110110"
k = 2
#s = "0110"
#k = 1
#s = "0110"
#k = 2
print(objeto.hasAllCodes(s, k))