class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        print(root.left)
        def dfs(node, maxVal):
            if not node:
                return 0
            #print('dentro =', node.val, 'maxval', maxVal, 'node.left',node.left,'node.right',node.right)
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        return dfs(root, root.val)

objeto = Solution()
#root = [3,1,4,3,None,1,5]
root = [3,3,None,4,2]

r = TreeNode(3, 3, None)
#r = TreeNode(3, 4, 2)
print(objeto.goodNodes(r))