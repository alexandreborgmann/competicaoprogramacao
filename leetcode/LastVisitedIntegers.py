from typing import List

class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        somaPrev = 0
        resultado = []
        #print(words)
        for i in range(len(words)):
            if words[i]=='prev':
                somaPrev += 1
                j = i-somaPrev+1
                z = 0
                while j>=0:
                    if words[j]!='prev':
                        z += 1
                        if z==somaPrev:
                            break
                    j -= 1
                    #print('j',j,'z',z,'words[j]=',words[j],'somaprev',somaPrev,'i=',i)
                #print('final j', j, 'z', z,'somaprev',somaPrev,'i',i)
                if j==-1:
                    resultado.append(-1)
                else:
                    resultado.append(int(words[j]))
            else:
                somaPrev = 0
            #print('i=',i,words[i],'somaPrev=',somaPrev,'resultado=',resultado)
        return(resultado)


objeto = Solution()
#words = ["1","prev","2","prev","prev"]
#words = ["1","2","prev","prev","prev"]
words = ["prev","prev","prev","27"]
print(objeto.lastVisitedIntegers(words))
