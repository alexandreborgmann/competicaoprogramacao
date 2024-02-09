class Solution:
    def firstUniqChar(self, s: str) -> int:
        conta = 0
        for i in s:
            if s.count(i) == 1:
                return(conta)
            conta += 1
        return -1


objeto = Solution()
s = "leetcode"
#s = "loveleetcode"
#s = "aabb"
print(objeto.firstUniqChar(s))