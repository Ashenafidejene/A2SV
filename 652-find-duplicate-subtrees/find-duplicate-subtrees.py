# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        visit = {}
        ans = []
        
        def dfs(node):
            if not node:
                return None
            temp = (node.val, dfs(node.left), dfs(node.right))
            if temp in visit:
                visit[temp] += 1
                if visit[temp] == 2:
                    ans.append(node)
            else:
                visit[temp] = 1
            return temp
        
        dfs(root)
        return ans 

