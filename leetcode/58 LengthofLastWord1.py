class Solution(object):
    def lengthOfLastWord(self, s):
        x = list(s.rstrip(' ').split(' '))
        return(len(x[-1]))

objeto = Solution()
s = "Hello World"
s = "   fly me   to   the moon  "
#s = "luffy is still joyboy"
if len(s)<1 or len(s)>=10**4:
    exit(1)
print(objeto.lengthOfLastWord(s))