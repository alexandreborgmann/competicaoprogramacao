class Solution:
    def removeTexto(self, x: str, c: str) -> str:
        i = 0
        lista = list(x)
        while len(lista)>0 and i<len(lista):
            if lista[i]==c:
                if i>0 and lista[i-1]!=c:
                    lista.pop(i-1)
                    lista.pop(i-1)
                    i -= 1
                else:
                    lista.pop(i)
            else:
                i += 1
            #print(i,lista,)
        return(''.join(lista))

    def backspaceCompare(self, s: str, t: str) -> bool:
        if self.removeTexto(s,'#') == self.removeTexto(t,'#'):
            return True
        else:
            return False

objeto = Solution()
s = "ab#c"
t = "ad#c"
'''
s = "ab##"
t = "c#d#"
s = "a#c"
t = "b"
'''
print(objeto.backspaceCompare(s, t))