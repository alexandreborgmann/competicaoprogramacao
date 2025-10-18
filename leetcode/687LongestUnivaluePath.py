from typing import List, Optional
from collections import deque

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node: Optional[TreeNode]):
        if not node:
            return (float("-inf"), 0)

        if not node.left and not node.right:
            return(node.val, 0)

        l_val, l_longest = self.dfs(node.left)
        r_val, r_longest = self.dfs(node.right)

        if l_val == r_val == node.val:
            self.res = max(self.res, 2 + l_longest + r_longest)
            return (node.val, 1 + max(l_longest, r_longest))
        elif l_val == node.val:
            self.res = max(self.res, 1 + l_longest)
            return (node.val, 1 + l_longest)
        elif r_val == node.val:
            self.res = max(self.res, 1 + r_longest)
            return (node.val, 1 + r_longest)
        else:
            return (node.val, 0)


objeto = Solution()
#root = [5,4,5,1,1,0,5]
#root = [1,4,5,4,4,0,5]
print(objeto.longestUnivaluePath(root))