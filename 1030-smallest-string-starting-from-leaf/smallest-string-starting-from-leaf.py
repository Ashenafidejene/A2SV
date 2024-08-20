# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        dic = {i: chr(97 + i) for i in range(26)}
        ans = []
        smalests = 8501
        def dfs(node,strs):
            if not node:
                return 
            strs = dic[node.val] + strs
            if node.left == None and node.right == None:
                ans.append(strs)
                return 
            dfs(node.left,strs)
            dfs(node.right,strs)
        dfs(root,"")
        return min(ans) if ans else ""
        