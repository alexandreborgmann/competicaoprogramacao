from typing import List, Optional
from collections import deque
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return None
        nodo = root
        print(nodo,root)
        resultado = []
        resultado.append(nodo.val)
        print(resultado)
        while nodo.right:
            nodo = nodo.right
            print('dentro',nodo.val,nodo.right)
            resultado.append(nodo.right)


        return resultado


objeto = Solution()
root = [1,2,3,None,5,None,4]
root = [1,None,3]
root = []

r = TreeNode(1,2,3)
r = TreeNode(2,None,5)
r = TreeNode(3,None,4)

print(objeto.rightSideView(r))