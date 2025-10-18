from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l = l + 1
            r = r - 1
        return True

objeto = Solution()
head = [1,2,2,1]
head = [1,2]
ln = []
for i in range(len(head)-1):
    ln.append(ListNode(head[i], head[i + 1]))
ln.append(ListNode(head[i], None))
i = 0
while ln[i].next:
    print(ln[i].val, ln[i].next)
    i += 1
print(objeto.isPalindrome(ln))
