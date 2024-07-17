# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []
        
        def preorder(node):
            if not node:
                return 
            ans.append(str(node.val))
            if not node.left and node.right:
                ans.append('()')
            if node.left:
                ans.append('(')
                preorder(node.left)
                ans.append(')')
            if node.right:
                ans.append('(')
                preorder(node.right)
                ans.append(')')
        
        preorder(root)
        return ''.join(ans)
        
            