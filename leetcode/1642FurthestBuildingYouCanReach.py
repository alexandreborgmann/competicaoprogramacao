import heapq
from typing import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            bricks -= diff
            heapq.heappush(heap, -diff)

            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -heapq.heappop(heap)
        return len(heights) - 1



heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1

heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2

heights = [14,3,19,3]
bricks = 17
ladders = 0

objeto = Solution()
print(objeto.furthestBuilding(heights, bricks, ladders))