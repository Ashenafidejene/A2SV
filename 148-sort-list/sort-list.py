# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def merge(left_half, right_half):
            dummy = ListNode(0)
            current = dummy
            while left_half and right_half:
                if left_half.val < right_half.val:
                    current.next = left_half
                    left_half = left_half.next
                else:
                    current.next = right_half
                    right_half = right_half.next
                current = current.next
            if left_half:
                current.next = left_half
            if right_half:
                current.next = right_half
            return dummy.next

        def get_mid(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def mergeSort(head):
            if not head or not head.next:
                return head
            mid = get_mid(head)
            right = mid.next
            mid.next = None
            left = mergeSort(head)
            right = mergeSort(right)
            return merge(left, right)

        return mergeSort(head)
    
   
