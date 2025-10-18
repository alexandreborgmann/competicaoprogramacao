from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        linhas, colunas = len(matrix), len(matrix[0])

        inicio, fim = 0, linhas - 1
        while inicio <= fim:
            linha = (inicio + fim) // 2
            if target > matrix[linha][-1]:
                inicio = linha + 1
            elif target < matrix[linha][0]:
                fim = linha - 1
            else:
                break

        if not (inicio <= fim):
            return False
        linha = (inicio + fim) // 2
        inicioc, fimc = 0, colunas - 1
        while inicioc <= fimc:
            meio = (inicioc + fimc) // 2
            if target > matrix[linha][meio]:
                inicioc = meio + 1
            elif target < matrix[linha][meio]:
                fimc = meio - 1
            else:
                return True
        return False

objeto = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
#matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
#target = 13
print(objeto.searchMatrix(matrix, target))