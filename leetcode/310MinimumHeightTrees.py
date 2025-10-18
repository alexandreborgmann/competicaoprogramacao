from collections import defaultdict
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        leaves = [node for node in graph.keys() if len(graph[node]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = set()
            for leave in leaves:
                neighbor = graph[leave].pop()
                graph[neighbor].remove(leave)
                if len(graph[neighbor]) == 1:
                    new_leaves.add(neighbor)
                leaves = new_leaves
        return leaves


objeto = Solution()
n = 4
edges = [[1,0],[1,2],[1,3]]
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(objeto.findMinHeightTrees(n, edges))