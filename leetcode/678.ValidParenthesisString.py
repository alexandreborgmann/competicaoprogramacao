class Solution:
    def checkValidString(self, s: str) -> bool:
        esquerdo = 0
        coringa = 0
        for i in range(len(s)):
            if s[i] == '*':
                coringa +=1
            elif s[i] == '(':
                esquerdo += 1
            elif s[i] == ')':
                if esquerdo == 0:
                    if coringa == 0:
                        return False
                    else:
                        coringa -= 1
                else:
                    esquerdo -= 1
            print(i,s[i],'esquerdo=',esquerdo,'coringa=',coringa)

        if esquerdo > coringa:
            return False
        else:
            return True

objeto = Solution()
#s = "()"
#s = "(*)"
#s = "(*))"
s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
print(objeto.checkValidString(s))