from collections import deque
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        q = deque()
        d = ListNode(0)
        d.next = head
        cur = d.next
        while cur:
            q.append(cur)
            cur = cur.next
        cur = dummy
        even = False
        while q:
            node = q.pop() if even else q.popleft()
            cur.next = None
            cur.next = node
            cur = cur.next
            even ^= True
        return head

objeto = Solution()
head = [1,2,3,4]
head = [1,2,3,4,5]
print(objeto.reorderList(head))
