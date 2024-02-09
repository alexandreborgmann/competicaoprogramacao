from typing import List
from collections import deque
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        queue = deque(range(1, 10))
        print(queue)
        while queue:
            n = queue.popleft()
            if n > high:
                continue
            if low <= n <= high:
                res.append(n)
            ones = n % 10
            if ones < 9:
                queue.append(n * 10 + (ones + 1))
            print(ones,n, res,queue)
        return res

low = 100
high = 300
#low = 1000
#high = 13000
objeto = Solution()
print(objeto.sequentialDigits(low, high))