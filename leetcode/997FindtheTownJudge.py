from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src, dst in trust:
            outgoing[src] += 1
            incoming[dst] += 1

        for i in range(1, n+1):
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i
        return -1


objeto = Solution()
n = 2
trust = [[1,2]]
n = 3
trust = [[1,3],[2,3]]
n = 3
trust = [[1,3],[2,3],[3,1]]
print(objeto.findJudge(n, trust))
