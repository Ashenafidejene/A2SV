# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is not None and q is not None:
            if p.val == q.val:
                first = self.isSameTree(p.left, q.left)
                second = self.isSameTree(p.right, q.right)
                return first and second
            else:
                return False
        elif p is None and q is None:
            return True
        else:
            return False