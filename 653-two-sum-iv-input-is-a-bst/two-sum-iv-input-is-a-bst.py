class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visit = set()
        
        def dfs(node):
            if not node:
                return False
            if k - node.val in visit:
                return True
            visit.add(node.val)
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)