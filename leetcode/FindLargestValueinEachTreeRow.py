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

        r = []
        q = deque([root])
        while q:
            #rint('q=',q,'r=',r)
            rmax =  q[0],val
            tamanho = len(q)
            for _ in range(tamanho):
                node = q.popleft()
                #print(type(node))
                rmax = max(rmax, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(rmax)
        return r

#objeto = Solution()
root = [1,2,3]
root = [1, 3, 2, 5, 3, 0, 9]
print(objeto.largestValues(root))
