class Solution:
    def sortSentence(self, s: str) -> str:
        lista = s.split(" ")
        retorno = ['']*len(lista)

        for i in range(len(lista)):
            indice = int(lista[i][-1])-1
            retorno[indice] = lista[i][0:-1]
        sr = ' '.join(retorno)
        return(sr)

objeto = Solution()
s = "is2 sentence4 This1 a3"
s = "Myself2 Me1 I4 and3"
print(objeto.sortSentence(s))