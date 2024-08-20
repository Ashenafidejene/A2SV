# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.MaxSum = float('-inf')
        def dfs(node):
            if not node :
                return 0
            Lsum = max(0,dfs(node.left))
            Rsum =max(0, dfs(node.right))
            tototal = node.val + Lsum + Rsum 
            self.MaxSum = max(self.MaxSum,tototal)
            return node.val + max(Lsum,Rsum)
        a = dfs(root)
        return self.MaxSum
            

