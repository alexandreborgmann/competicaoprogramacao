from typing import List

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        pass

objeto = Solution()
n = 5
edges = [[0,1,7],[1,3,7],[1,2,1]]
query = [[0,3],[3,4]]
n = 3
edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]]
query = [[1,2]]
print(objeto.minimumCost(n, edges, query))