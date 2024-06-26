# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        def levelOrderHelper(node: Optional[TreeNode], level: int):
            if not node:
                return
            if len(ans) == level:
                ans.append([])
            ans[level].append(node.val)
            levelOrderHelper(node.left, level + 1)
            levelOrderHelper(node.right, level + 1)
        
        levelOrderHelper(root, 0)
        return ans
      