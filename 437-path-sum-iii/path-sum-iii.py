# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.counter = 0
        
        def dfs(node, sums):
            if not node:
                return
            
            sums += node.val
            
            if sums == targetSum:
                self.counter += 1
            
            # Continue the path
            dfs(node.left, sums)
            dfs(node.right, sums)
        
        def traverse(node):
            if not node:
                return
            dfs(node, 0)  
            traverse(node.left)  
            traverse(node.right) 
        
        traverse(root)
        return self.counter