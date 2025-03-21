# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maxs = 0
        stack = []
        def dfs(root):
            if not root:
                return 
            stack.append(root.val)
            self.maxs = max(self.maxs , (max(stack)-min(stack)))
            dfs(root.left)
            dfs(root.right)
            stack.pop()
        dfs(root)
        return self.maxs