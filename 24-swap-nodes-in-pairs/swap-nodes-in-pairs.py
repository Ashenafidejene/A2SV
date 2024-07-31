# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
       def recursion(node):
            if not node or not node.next:
                return node
            first = node
            second = node.next
            first.next = recursion(second.next)
            second.next = first
            return second
       return recursion(head)