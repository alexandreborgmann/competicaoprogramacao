class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
                print('while','r',r,'l',l,'charSet',charSet,'res',res)
            charSet.add(s[r])
            res = max(res, r - l +1)
            print('r',r,'l',l,'charSet',charSet,'res',res)
        return res
objeto = Solution()
#s = "abcabcbb"
#s = "bbbbb"
s = "pwwkew"
#s = " "
#s = "au"
#s = "dvdf"
print(objeto.lengthOfLongestSubstring((s)))