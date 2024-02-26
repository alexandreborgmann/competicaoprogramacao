class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        parAbre = parFecha = 0

        resultado = []

        for letra in s:
            if letra == '(':
                parAbre +=1
                resultado.append(letra)
            elif letra ==')':
                if parAbre > parFecha:
                    parFecha +=1
                    resultado.append(letra)
            else:
                resultado.append(letra)
        #print(resultado)
        if parAbre ==parFecha:
            return "".join(resultado)
        else:
            resultadoFinal = []
            for i in range(len(resultado) -1, -1, -1):
                letra = resultado[i]
                if letra == '(':
                    if parAbre <= parFecha:
                        resultadoFinal.append(letra)
                    else:
                        parAbre -= 1
                elif letra == ')':
                    resultadoFinal.append(letra)
                else:
                    resultadoFinal.append(letra)
            return "".join(reversed(resultadoFinal))

objeto = Solution()
s = "lee(t(c)o)de)"
#s = "a)b(c)d"
#s = "))(("
print(objeto.minRemoveToMakeValid(s))