from typing import Optional
'''
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
'''
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.total = 0
        def dfs(node, left):
            if not node:
                return
            dfs(node.left, True)
            dfs(node.right, False)
            if not node.left and not node.right and left:
                self.total += node.val

        dfs(root, False)
        return self.total


objeto = Solution()
root = [3,9,20,None,None,15,7]
root = [1]
print(objeto.sumOfLeftLeaves(root))

