# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node,sums):
            if not node :
               return False 
            sums+=node.val
            if node.left == None and node.right== None :
                return sums ==  targetSum
            return dfs(node.left,sums) or dfs(node.right,sums)
        if not root :
            return False 

        return dfs(root,0)
            