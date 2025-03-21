# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            level = []
            if len(result) % 2 == 1 :
               for i in range(len(queue)):
                  queue[i].val = result[-1][len(result[-1])-1-i]
            for _ in range(level_size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    level.append(node.right.val)
                    queue.append(node.right)
            
            result.append(level)
            left_to_right = not left_to_right

        return root