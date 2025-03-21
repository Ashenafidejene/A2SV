# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        def inorder(root):
            if root is None :
                return 
            inorder(root.left)
            stack.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(len(stack)-1):
            if stack[i] >= stack[i+1]:
                return False 
        return True 

        