# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            dfs(node.right)
            Nleft = node.left
            Nright = node.right
            node.left = None 
            node.right = Nleft
            while node.right:
                node = node.right
            node.right = Nright
        dfs(root)



        """
        Do not return anything, modify root in-place instead.
        """
        
        