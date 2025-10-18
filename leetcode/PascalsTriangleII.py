from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
           return([1])
        for i in range(1,rowIndex+1):
            atual = [0] * (i + 1)
            for z in range(i+1):
                if z==0 or z==i:
                    atual[z] = 1
                    #print('i=', i, 'z=', z)
                else:
                    atual[z] = anterior[z-1] + anterior[z]
                    #print('i=',i,'z=',z,anterior[z-1],anterior[z])
            anterior = atual
        return(atual)

#owIndex = 3
#rowIndex = 0
rowIndex = 1
objeto = Solution()
print(objeto.getRow(rowIndex))
