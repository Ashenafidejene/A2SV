# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        slow = head
        fast = head

        # Find the meeting point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:  # No cycle found
            return None

        # Move one pointer back to the head
        slow = head

        # Move both pointers at the same pace until they meet again
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow