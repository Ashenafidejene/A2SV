# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        # Initialize the heap with the head of each list
        for index, list_node in enumerate(lists):
            if list_node is not None:
                heapq.heappush(min_heap, (list_node.val, index, list_node))
        
        dummy = ListNode()
        current = dummy
        
        while min_heap:
            val, index, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next is not None:
                heapq.heappush(min_heap, (node.next.val, index, node.next))
        
        return dummy.next
