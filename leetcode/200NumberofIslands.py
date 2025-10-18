from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])

        used = [[False] * C for _ in range(R)]
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def visit(x, y):
            used[x][y] = True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny <= C and not used[nx][ny] and grid[x][y] == '1':
                    visit(nx, ny)

        count = 0
        for x in range(R):
            for y in range(C):
                if not used[x][y] and grid[x][y] == "1":
                    count += 1
                    visit(x, y)

        return count

objeto = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(objeto.numIslands(grid))
