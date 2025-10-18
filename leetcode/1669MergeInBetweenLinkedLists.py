def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        i = 0
        while i < a - 1:
            curr = curr.next
            i += 1

        head = curr
        while i <= b:
            curr = curr.next
            i += 1
        head.next = list2

        while list2.next:
            list2 = list2.next
        list2.next = curr
        return list1

objeto = Solution()
list1 = [10,1,13,6,9,5]
a = 3
b = 4
list2 = [1000000,1000001,1000002]
list1 = [0,1,2,3,4,5,6]
a = 2
b = 5
list2 = [1000000,1000001,1000002,1000003,1000004]
print(objeto.mergeInBetween(list1, a, b, list2))
