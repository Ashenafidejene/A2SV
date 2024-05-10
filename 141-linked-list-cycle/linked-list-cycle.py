# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:  # Corrected from 'null' to 'None'
            return False 
        slowest = head.next  
        fastest = head.next
        while fastest and fastest.next:  # Added condition to check if 'fastest' and 'fastest.next' are not None
            fastest = fastest.next.next 
            slowest = slowest.next 
            if fastest == slowest:
                return True
            
        return False 