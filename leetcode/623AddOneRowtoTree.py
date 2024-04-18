# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        def dfs(node, depth_left):
            if node is None:
                return
            if depth_left == 1:
                old_left = node.left
                old_right = node.right

                node.left = TreeNode(val, left=old_left)
                node.right = TreeNode(val, right=old_right)
                return
            dfs(node.left, depth_left - 1)
            dfs(node.right, depth_left - 1)

        dfs(root, depth - 1)
        return root

objeto = Solution()
root = [4,2,6,3,1,5]
val = 1
depth = 2
root = [4,2,None,3,1]
val = 1
depth = 3
print(objeto.addOneRow(root, val, depth))