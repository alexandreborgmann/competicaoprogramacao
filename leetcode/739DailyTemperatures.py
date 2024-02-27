from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        resultado = []
        tamanho = len(temperatures)-1
        for i in range(tamanho):
            j = i+1
            conta = 0
            achou = 0
            #print('inicio','i=',i, 'j=',j, tamanho, 'conta=', conta,'temperatures[i]',temperatures[i],'temperatures[j]',temperatures[j],'tamanho',tamanho)
            while j<=tamanho:
                conta += 1
                if temperatures[j]>temperatures[i]:
                    achou = 1
                    break
                j +=1
                #print(i, j, tamanho, 'conta=',conta,'temperatures[i]',temperatures[i],'temperatures[j]',temperatures[j])
            if achou == 1:
                resultado.append(conta)
            else:
                resultado.append(0)
        resultado.append(0)
        return(resultado)

objeto = Solution()
#temperatures = [73,74,75,71,69,72,76,73]
#temperatures = [30,40,50,60]
temperatures = [30,60,90]
print(objeto.dailyTemperatures(temperatures))
