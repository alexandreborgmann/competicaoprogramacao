class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n <= bad:
            return n
        for i in range(1, n+1):
            if isBadVersion(i):
                return i

objeto = Solution()
#n = 5
#bad = 4
#n = 1
#bad = 1
n = 2
bad = 1
print(objeto.firstBadVersion(n))