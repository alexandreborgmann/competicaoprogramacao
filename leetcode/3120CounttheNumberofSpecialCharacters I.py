class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word.lower())
        conta = 0
        for i in s:
            if i.upper() in word and i.lower() in word:
                conta += 1
            #print(i,word,i.upper(),i.lower(),conta,i.upper() in word,i.lower() in word )
        return conta


objeto = Solution()
word = "aaAbcBC"
#word = "abc"
#word = "abBCab"
print(objeto.numberOfSpecialChars(word))