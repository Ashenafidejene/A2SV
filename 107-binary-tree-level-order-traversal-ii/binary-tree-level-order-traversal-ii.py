# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
           return []
        
        queue = deque([root])
        levels = []
        while queue:
            levels.append([node.val for node in queue])
            length = len(queue)
            for _ in range(length):
                nodes = queue.popleft()
                if nodes.left :
                    queue.append(nodes.left)
                if nodes.right:
                    queue.append(nodes.right)
        levels.reverse()
        return levels
