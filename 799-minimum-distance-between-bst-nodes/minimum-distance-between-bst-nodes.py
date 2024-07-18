# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('inf')
        self.prev_val = -float('inf')

        def in_order_traversal(node):
            if not node:
                return

            in_order_traversal(node.left)

    
            self.min_diff = min(self.min_diff, node.val - self.prev_val)
            self.prev_val = node.val

            in_order_traversal(node.right)

        in_order_traversal(root)
        return self.min_diff
             

          


        