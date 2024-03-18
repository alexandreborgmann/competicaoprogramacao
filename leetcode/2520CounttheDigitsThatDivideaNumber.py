class Solution:
    def countDigits(self, num: int) -> int:
        lista = str(num)
        conta = 0
        for i in lista:
            if num % int(i) == 0:
                conta +=1
        return conta

objeto = Solution()
num = 7
#num = 121
#num = 1248
print(objeto.countDigits(num))