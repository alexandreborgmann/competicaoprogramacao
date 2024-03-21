from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        res = len(points)
        prev = points[0]
        for i in range(1, len(points)):
            curr = points[i]
            if curr[0] <= prev[1]:
                res -= 1
                prev = [curr[0],min(curr[1],prev[1])]
            else:
                prev = curr

        return res

objeto = Solution()
points = [[10,16],[2,8],[1,6],[7,12]]
#points = [[1,2],[3,4],[5,6],[7,8]]
#points = [[1,2],[2,3],[3,4],[4,5]]
print(objeto.findMinArrowShots(points))