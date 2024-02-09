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

            ans = []
            queue = deque([root])

            while queue:
                current_length = len(queue)
                curr_max = float("-inf")

                for _ in range(current_length):
                    node = queue.popleft()
                    curr_max = max(curr_max, node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                ans.append(curr_max)

            return ans

objeto = Solution()
root = [1,2,3]
root = [1, 3, 2, 5, 3, 0, 9]
print(objeto.largestValues(root))
