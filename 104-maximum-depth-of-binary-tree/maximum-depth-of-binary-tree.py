# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def Depth(node: Optional[TreeNode], depth: int) -> int:
            if not node:
                return depth
            
            depth += 1
            left_depth = Depth(node.left, depth)
            right_depth = Depth(node.right, depth)
            
            return max(left_depth, right_depth)
        
        return Depth(root, 0)