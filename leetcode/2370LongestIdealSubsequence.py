class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        cache = {}
        def helper(i, prev):
            if i == len(s):
                return 0
            if (i, prev) in cache:
                return cache[(i, prev)]
            res = helper(i + 1, prev)
            if prev == "" or abs(ord(s[i]) - ord(prev)) <=k:
                res = max(res, 1 + helper(i + 1, s[i]))
            cache[(i, prev)] = res
            return res

        return helper(0, "")

objeto = Solution()
s = "acfgbd"
k = 2
#s = "abcd"
#k = 3
print(objeto.longestIdealString(s, k))