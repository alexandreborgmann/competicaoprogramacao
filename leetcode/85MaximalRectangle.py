from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        pass
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def getMaxAreaHisto(histogram):
            n = len(histogram)
            left_lim = [0]*n
            right_lim = [0]*n
            left_lim[0] = -1
            right_lim[n-1] = n
            max_histo_area = 0

            for i in range(1, n):
                pointer = i-1
                while (pointer >= 0) and (histogram[pointer] >= histogram[i]):
                    pointer = left_lim[pointer]
                left_lim[i] = pointer

            for i in range(n-2, -1, -1):
                pointer = i+1
                while (pointer < n) and (histogram[pointer] >= histogram[i]):
                    pointer = right_lim[pointer]
                right_lim[i] = pointer

            for i in range(n):
                height = histogram[i]
                width = right_lim[i] - left_lim[i] - 1
                max_histo_area = max(max_histo_area, height*width)

            return max_histo_area

        def getHistoArea(rows):
            cols = len(rows[0])
            histogram = [0]*cols
            for row in rows:
                for col in range(cols):
                    histogram[col] = 0 if row[col] == '0' else (
                        1 + histogram[col])
            return getMaxAreaHisto(histogram)

        max_area = 0
        rows = len(matrix)
        if rows < 1:
            return 0

        for r in range(rows):
            max_area = max(max_area, getHistoArea(matrix[:r+1]))
        return max_area
objeto = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#matrix = [["0"]]
#matrix = [["1"]]
print(objeto.maximalRectangle(matrix))