# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Merges two sorted linked lists
        def merge(list1, list2):
            dummy = ListNode()
            tail = dummy
            while list1 is not None and list2 is not None:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            if list1 is not None:
                tail.next = list1
            else:
                tail.next = list2
            return dummy.next
        
        # Recursive merge sort for the list of linked lists
        def mergeSort(arr, left, right):
            if left == right:
                return arr[left]
            mid = left + (right - left) // 2
            left_half = mergeSort(arr, left, mid)
            right_half = mergeSort(arr, mid + 1, right)
            return merge(left_half, right_half)
        
        if not lists:
            return None
        
        return mergeSort(lists, 0, len(lists) - 1)
