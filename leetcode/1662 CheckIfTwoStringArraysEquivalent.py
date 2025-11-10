from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ""
        for i in range(len(word1)):
            s1=s1+word1[i]
        s2 = ""
        for i in range(len(word2)):
            s2=s2 + word2[i]
        #print(s1,s2)
        if s1 == s2:
            return(True)
        else:
            return(False)

objeto = Solution()
word1 = ["ab", "c"]
word2 = ["a", "bc"]
'''
word1 = ["a", "cb"]
word2 = ["ab", "c"]
word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]
'''
print(objeto.arrayStringsAreEqual(word1, word2))