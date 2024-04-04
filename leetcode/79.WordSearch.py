from typing import List

class Solution:
    def dfs(self, board, word, r, c, i):
        if i >= len(word):
            return True
        if r >= len(board) or r < 0 or c >= len(board[0]) or c < 0 or board[r][c]!= word[i]:
            return False
        l = board[r][c]
        board[r][c] = ""
        achou = self.dfs(board, word, r-1, c, i+1) or self.dfs(board, word, r+1, c, i+1) or \
        self.dfs(board, word, r, c+1, i + 1) or self.dfs(board, word, r, c-1, i + 1)
        board[r][c] = l
        return achou

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, word, i, j, 0):
                    return True
        return False

objeto = Solution()
#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = "ABCCED"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word= "AAB"
print(objeto.exist(board, word))