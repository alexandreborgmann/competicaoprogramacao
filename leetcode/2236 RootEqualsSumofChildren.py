
'''
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.left.val + root.right.val == root.val
'''

class Solution:
    def __init__(self, val=0, left=None, right=None):
             self.val = val
             self.left = left
             self.right = right

    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if self.left+self.right != self.val:
            return False
        return True

#objeto = Solution(5,3,1)
objeto = Solution(10, 4, 6)
print(objeto.checkTree())