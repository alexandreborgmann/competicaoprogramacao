from typing import List

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == -1:
                    maior = -1
                    for linha in range(len(matrix)):
                        maior = max(maior, matrix[linha][j])
                    matrix[i][j] = maior
        return matrix

objeto = Solution()
#matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
#matrix = [[3,-1],[5,2]]
matrix = [[2,-1,2,-1,2],[1,0,-1,2,-1],[2,-1,-1,-1,2],[2,1,2,-1,2],[0,1,0,0,0],[0,0,0,0,-1],[2,-1,2,2,0],[0,1,0,2,2],[2,2,0,1,-1]]
print(objeto.modifiedMatrix(matrix))