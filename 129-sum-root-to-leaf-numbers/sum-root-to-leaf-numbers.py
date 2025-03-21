# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        result = []
        def dfs(node,strs):
            strs = strs + str(node.val)
            if not(node.right or node.left):
                result.append(strs)
            if node.right :
                dfs(node.right , strs)
            if node.left :
                dfs(node.left,strs)
        dfs(root,"")
        ans = 0 
        for num in result :
            ans += int(num)
        return ans 

