from typing import List,Optional
from collections import deque
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            current = stack.pop()
            result.append(current.val)

            if current.left:
                stack.append(current.left)

            if current.right:
                stack.append(current.right)

        return result[::-1]

objeto = Solution()
root = [1,None,2,3]
root = []
root = [1]
print(objeto.postorderTraversal(deque([root])))