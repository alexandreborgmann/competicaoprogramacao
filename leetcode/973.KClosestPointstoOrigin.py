import heapq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2 ) + (y ** 2)
            minHeap.append([dist, x, y])
        print(minHeap)
        heapq.heapify(minHeap)
        res = []
        print(minHeap)
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            #print(dist,x,y)
            res.append([x,y])
            k -= 1
        return res

objeto = Solution()
points = [[1,3],[-2,2]]
k = 1
points = [[3,3],[5,-1],[-2,4]]
k = 2
print(objeto.kClosest(points, k))