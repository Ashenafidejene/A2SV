# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(node , strs):
            if not node : 
                return 
            strs += str(node.val)
            if not node.right and not node.left:
                ans.append(strs)
                return 
            dfs(node.left,strs)
            dfs(node.right,strs)
        dfs(root,'')
        sums =  0 
        for num  in ans:
            sums += int(num,2)
        return sums