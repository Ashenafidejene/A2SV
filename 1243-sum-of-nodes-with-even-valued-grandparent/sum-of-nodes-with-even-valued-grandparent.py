# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        parent = []
        sum = [0]
        def dfs(node):
            if not node :
               return 
            
            if len(parent) >= 2:
               if parent[len(parent)-2]%2 ==0:
                  sum[0]+=node.val
            parent.append(node.val)
            dfs(node.left)
            dfs(node.right)
            parent.pop()
        dfs(root)
        return sum[0]


            