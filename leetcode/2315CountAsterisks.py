class Solution:
    def countAsterisks(self, s: str) -> int:
        if s.find('|') == -1:
            return s.count('*')
        inicio = 0
        fim = 0
        while True:
            inicio = s.find('|')
            if inicio == -1:
                break
            fim = s.find('|',inicio+1)
            if fim == -1:
                break
            if inicio == 0:
                s = s[fim+1:]
            else:
                s = s[0:inicio]+s[fim+1:]
        return s.count('*')

objeto=Solution()
s = "l|*e*et|c**o|*de|"
#s = "iamprogrammer"
#s = "yo|uar|e**|b|e***au|tifu|l"
#s = "|**|*|*|**||***||"
s = "*jsaxclgfcyjds"
print(objeto.countAsterisks(s))
