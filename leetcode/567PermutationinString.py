class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:        ''''''
        s3 = s1[::-1]
        print(s3,s2.find(s3),s2)
        if s2.find(s3) != -1 or s2.find(s1) != -1:
            return True
        else:
            return False

objeto = Solution()
#s1 = "ab"
#s2 = "eidbaooo"
#s1 = "ab"
#s2 = "eidboaoo"
#s1 = "ab"
#s2 = "ab"
s1 = "abc"
s2 = "bbbca"
print(objeto.checkInclusion(s1, s2))
