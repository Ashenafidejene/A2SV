# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(node, flag):
            if not node:
                return 0
            if (node, flag) in memo:
                return memo[(node, flag)]
            if flag:
                rob = node.val + dp(node.left, False) + dp(node.right, False)
                not_rob = dp(node.left, True) + dp(node.right, True)
                memo[(node, flag)] = max(rob, not_rob)
            else:
                not_rob = dp(node.left, True) + dp(node.right, True)
                memo[(node, flag)] = not_rob
            return memo[(node, flag)]
        
        return dp(root, True)