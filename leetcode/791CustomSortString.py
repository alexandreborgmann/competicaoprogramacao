class Solution:
    def customSortString(self, order: str, s: str) -> str:
        resultado = ""
        for letra in order:
            if letra in s:
                conta = s.count(letra)
                s = s.replace(letra,'')
                resultado += letra*conta
        resultado += s
        return resultado

objeto = Solution()
#order = "cba"
#s = "abcd"
#order = "bcafg"
#s = "abcd"
order = "kqep"
s = "pekeq"
print(objeto.customSortString(order, s))