# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node,ch):
            if not node:
                return
            ch.append(node.val)
            if node.left == None and node.right == None :
                if sum(ch) == targetSum:
                    ans.append(ch.copy())
            dfs(node.left,ch)
            dfs(node.right,ch)
            ch.pop()
        dfs(root,[])
        return ans

                
            
