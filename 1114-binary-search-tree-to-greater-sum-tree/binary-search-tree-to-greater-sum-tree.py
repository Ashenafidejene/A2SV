# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sums = 0 
        def SumDfs(node):
            if not node :
                return 
            self.sums+= node.val
            SumDfs(node.left)
            SumDfs(node.right)
        ans = []
        def dfs(node):
            if not node :
                return 
            dfs(node.left)
            x = node.val 
            node.val = self.sums
            self.sums-=x 
            dfs(node.right)
        SumDfs(root)
        dfs(root)
        return root
            
