# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root :
            return False
        def handler(temp,linkeds):
            if not temp:
                return True
            if not linkeds or temp.val != linkeds.val:
                return False
            return (handler(temp.next,linkeds.left) or handler(temp.next,linkeds.right))
        if handler(head,root):
            return True
        return(self.isSubPath(head,root.right) or self.isSubPath(head,root.left))
    

