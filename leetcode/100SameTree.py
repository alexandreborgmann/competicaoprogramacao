from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if (p and q and p.val != q.val) or p is None or q is None:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

objeto = Solution()
p = [1, 2, 3]
q = [1, 2, 3]
p = [1,2]
q = [1, None, 2]
p = [1,2,1]
q = [1,1,2]
print(objeto.isSameTree(p, q))