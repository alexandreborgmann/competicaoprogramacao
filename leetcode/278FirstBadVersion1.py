class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n

        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return r


objeto = Solution()
#n = 5
#bad = 4
#n = 1
#bad = 1
n = 2
bad = 1
print(objeto.firstBadVersion(n))