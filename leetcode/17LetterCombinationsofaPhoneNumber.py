from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        DigitoLetras = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

        combinacoes = []
        if len(digits) == 0:
            return combinacoes

        if len(digits)==1:
            combinacoes = list(DigitoLetras[int(digits)])
        else:
            listaDigito = list(digits)
            combinacoes = []*len(listaDigito)
            for i in range(len(listaDigito)):
                combinacoes.append("")
            for i in range(len(listaDigito)):
                for j in range(i+1,)
                combinacoes[i] = combinacoes[i]+DigitoLetras[int(listaDigito[i])][0]
                combinacoes[i] = combinacoes[i] + DigitoLetras[int(listaDigito[i])][1]
                combinacoes[i] = combinacoes[i] + DigitoLetras[int(listaDigito[i])][2]

        return(combinacoes)
objeto = Solution()
#digits ="234"
digits = "23"
#digits = ""
#digits = "2"
print(objeto.letterCombinations(digits))


'''
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        DigitoLetras = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

        combinacoes = []
        if len(digits) == 0:
            return combinacoes

        if len(digits)==1:
            combinacoes = list(DigitoLetras[int(digits)])
        else:
            listaDigito = list(digits)
            for i in range(len(listaDigito)):
                for j in range(i+1,len(listaDigito)):
                    for z in range(3):
                        for y in range(3):
                            #print(i,'j=',j,z,listaDigito)
                            combinacoes.append(DigitoLetras[int(listaDigito[i])][z] + DigitoLetras[int(listaDigito[j])][y])
        return(combinacoes)
objeto = Solution()
digits = "23"
#digits = ""
#digits = "2"
print(objeto.letterCombinations(digits))

'''