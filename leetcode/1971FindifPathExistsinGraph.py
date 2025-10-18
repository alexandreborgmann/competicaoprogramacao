import collections
from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        done = set()
        q = collections.deque()
        adj_list = collections.defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        done.add(source)
        q.append(source)

        while len(q) > 0:
            now = q.popleft()
            for v in adj_list[now]:
                if v not in done:
                    done.add(v)
                    q.append(v)
        return destination in done

objeto = Solution()
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
'''
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
'''
print(objeto.validPath(n,edges,source,destination))
