from typing import List, Optional
from collections import deque


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        temp = [root]
        ans = []
        while temp:
            ans.append(max([_.val for _ in temp]))
            new = []
            for item in temp:
                if item.left:
                    new.append(item.left)
                if item.right:
                    new.append(item.right)
            temp = new
        return ans

objeto = Solution()
root = [1,2,3]
root = [1, 3, 2, 5, 3, 0, 9]
print(objeto.largestValues(root))
