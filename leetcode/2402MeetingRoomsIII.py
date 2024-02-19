import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)]
        used = []
        count = [0] * n

        for start, end in meetings:
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + ( end - start)
                heapq.heappush(available, room)

            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1

        return count.index(max(count))



objeto = Solution()
n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]
#n = 3
#meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
print(objeto.mostBooked(n, meetings))
