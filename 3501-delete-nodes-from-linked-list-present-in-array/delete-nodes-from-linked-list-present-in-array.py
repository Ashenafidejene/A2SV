# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        # Convert nums to a set for O(1) lookup time
            nums_set = set(nums)
            
            # Use a dummy node to handle edge cases easily
            dummy = ListNode(0)
            dummy.next = head
            
            # Initialize pointers
            prev, current = dummy, head
            
            # Traverse the linked list
            while current:
                if current.val in nums_set:
                    # Skip the current node by linking prev to current.next
                    prev.next = current.next
                else:
                    # Move prev to current only if current is not deleted
                    prev = current
                
                # Move to the next node
                current = current.next
            
            # Return the modified list starting from dummy.next
            return dummy.next  