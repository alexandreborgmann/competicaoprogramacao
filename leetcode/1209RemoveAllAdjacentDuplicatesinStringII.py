class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        trocou = 1
        while trocou:
            trocou = 0
            i = 0
            while i <= len(s)-k:
                #print('entrei',i,s[i]*k,s[i:i+k],s)
                if s[i]*k == s[i:i+k]:
                    trocou = 1
                    if i>0:
                        s = s[0:i] + s[i+k:]
                    else:
                        s = s[i+k:]
                i += 1
                #print(s,i)
        return(s)

objeto = Solution()
#s = "abcd"
#k = 2
#s = "deeedbbcccbdaa"
#k = 3
s = "pbbcggttciiippooaais"
k = 2
#s = "yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy"
#k = 4
print(objeto.removeDuplicates(s, k))