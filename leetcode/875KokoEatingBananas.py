import math
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res



objeto = Solution()
#piles = [3,6,7,11]
#h = 8
piles = [30,11,23,4,20]
h = 5
#piles = [30, 11, 23, 4, 20]
#h = 6
print(objeto.minEatingSpeed(piles, h))