# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rightPtr = head 
        while n > 0 : 
            rightPtr= rightPtr.next 
            n-=1
        leftPtr = head 
        ptr = None
        while rightPtr:
            ptr = leftPtr 
            leftPtr = leftPtr.next 
            rightPtr = rightPtr.next 
        if ptr:
            ptr.next = leftPtr.next 
        else:
            head = head.next 
        return head 
        

