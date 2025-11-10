'''
You are given an array of integers nums and the head of a linked list.
Return the head of the modified linked list after removing all nodes from
the linked list that have a value that exists in nums.

Example 1:

Input: nums = [1,2,3], head = [1,2,3,4,5]

Output: [4,5]

Explanation:

Remove the nodes with values 1, 2, and 3.

Example 2:
Input: nums = [1], head = [1,2,1,2,1,2]

Output: [2,2,2]

Explanation:

Remove the nodes with value 1.

Example 3:

Input: nums = [5], head = [1,2,3,4]

Output: [1,2,3,4]

Explanation:

No node has value 5.
'''
from typing import List, Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0, head)
        prev = dummy
        #print(prev.val,prev.next)
        while prev.next:
            #print(prev.val, prev.next, prev.next.val)
            if prev.next.val in nums:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next

def create_linked_list(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

objeto = Solution()
nums = [1,2,3]
head = [1,2,3,4,5]

# [4,5]
nums = [1]
head = [1,2,1,2,1,2]
# [2,2,2]
#nums = [5]
#head = [1,2,3,4]
# [1,2,3,4]

head_linked_list = create_linked_list(head)
head_ll_result = objeto.modifiedList(nums, head_linked_list)
print(linked_list_to_list(head_ll_result))
