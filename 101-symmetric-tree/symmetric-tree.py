# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
           return False 
        
        def isSymmetricP(p,q):
            if not (p or q):
                return True
            if p is None or q is None :
                return False 
            if p.val == q.val :
                return isSymmetricP(p.right,q.left) and isSymmetricP(p.left,q.right)
            else:
                return False 
        return isSymmetricP(root.right,root.left)