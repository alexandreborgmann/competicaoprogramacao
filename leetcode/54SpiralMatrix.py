from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        min_c = 0
        max_c = len(matrix[0])
        min_l = 0
        max_l = len(matrix)
        l = 0
        r = []
        while min_c < max_c and min_l < max_l:
            for c in range(min_c,max_c):
                r.append(matrix[l][c])
            min_l += 1

            for l in range(min_l,max_l):
                r.append(matrix[l][c])
            max_c -= 1
            if min_c < max_c and min_l < max_l:
                for c in range(max_c-1, min_c-1, -1):
                    r.append(matrix[l][c])
                max_l -= 1

                for l in range(max_l -1 ,min_l -1, -1):
                    r.append(matrix[l][c])
                min_c += 1
        return r

objeto = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(objeto.spiralOrder(matrix))