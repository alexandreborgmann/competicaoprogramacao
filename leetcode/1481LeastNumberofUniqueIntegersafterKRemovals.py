import heapq
from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        heap = list(freq.values())
        heapq.heapify(heap)
        #print(freq, heap,freq.values())

        res = len(heap)
        while k > 0 and heap:
            f = heapq.heappop(heap)
            if k >= f:
                k -=f
                res -=1
            #print(k,'f=',f,heap)
        return res

objeto = Solution()
arr = [5,5,4]
k = 1
#arr = [4,3,1,1,3,3,2]
#k = 3
print(objeto.findLeastNumOfUniqueInts(arr, k))