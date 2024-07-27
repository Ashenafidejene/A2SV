# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = []
        self.sums = 0 
        def dfs(node , strs):
            if not node : 
                return 
            strs += str(node.val)
            if not node.right and not node.left:
                self.sums += int(strs,2)
                return 
            dfs(node.left,strs)
            dfs(node.right,strs)
        dfs(root,'')
        return self.sums