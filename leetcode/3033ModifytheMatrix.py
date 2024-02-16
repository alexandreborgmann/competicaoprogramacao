from typing import List

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == -1:
                    maior = 0
                    for linha in range(len(matrix)):
                        maior = max(maior, matrix[linha][j])
                    matrix[i][j] = maior
        return matrix

objeto = Solution()
#matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
matrix = [[3,-1],[5,2]]
print(objeto.modifiedMatrix(matrix))