# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
               return self.inorder(root)
    
    def inorder(self, node: Optional[TreeNode]) -> bool:
        if node is None:
            return True
        
        if not self.inorder(node.left):
            return False
        
        if self.prev is not None and node.val <= self.prev:
            return False
        
        self.prev = node.val
        
        return self.inorder(node.right)
 