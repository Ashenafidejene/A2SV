# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sums = [0]

        def dfs(node , number):
            if not node :
               return 
            number = number*10 + node.val
            if not node.right and not node.left:
                sums[0] += number 
                return 
            dfs(node.left , number)
            dfs(node.right, number)
        dfs(root,0,)
        return sums[0]
        