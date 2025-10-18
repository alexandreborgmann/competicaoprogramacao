class Solution:
    def pivotInteger(self, n: int) -> int:
        numeros = []

        for i in range(1,n + 1):
            numeros.append(i)

        for pivot in range(n):
            antesPivot = sum(numeros[:pivot + 1])
            depoisPivot = sum(numeros[pivot:])
            if antesPivot == depoisPivot:
                return pivot + 1

        return -1

objeto = Solution()
n = 8
#n = 1
#n = 4
print(objeto.pivotInteger(n))