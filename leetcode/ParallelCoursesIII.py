from typing import List
from collections import defaultdict

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        for src, dst in relations:
            adj[src].append(dst)
        #print(adj)

        maxTime = {}
        def dfs(src):
            if src in maxTime:
                return maxTime[src]

            res = time[src - 1]
            for nei in adj[src]:
               res = max(res,time[src - 1] + dfs(nei))
            maxTime[src] = res
            return res

        for i in range(1, n+1):
            dfs(i)

        return max(maxTime.values())
objeto = Solution()
'''
n = 3
relations = [[1,3],[2,3]]
time = [3,2,5]
'''
n = 5
relations = [[1,5],[2,5],[3,5],[3,4],[4,5]]
time = [1,2,3,4,5]

print(objeto.minimumTime(n, relations, time))