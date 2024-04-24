class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        conta = 0
        imai = 0
        imin = 0
        while len(word) > 0:
            c = word[0]
            if c == c.lower():
                try:
                    imai = word.index(c.upper(),1)
                except:
                    imai = 0
                try:
                    imin = word.index(c,max(1,imai))
                except:
                    imin = 0
                if imai == 0:
                    word = word.replace(c.lower(), '')
                    word = word.replace(c.upper(), '')
                else:
                    if imin == 0:
                        conta += 1
                    word = word.replace(c.lower(), '',1)
                    word = word.replace(c.upper(), '', 1)
            else:
                word=word.replace(c.lower(),'')
                word=word.replace(c.upper(), '')
            #print('word=',word,c,'conta=',conta,imai,imin)
        return conta
objeto = Solution()
word = "aaAbcBC"
#word = "abc"
#word = "AbBCab"
print(objeto.numberOfSpecialChars(word))