# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val 
        queue = deque([[root]])
        while queue :
            temp = queue.popleft()
            temp1 = []
            for  node in temp :
                if node.val != val :
                    return False 
                if node.left :
                    temp1.append(node.left)
                if node.right :
                    temp1.append(node.right)
            if temp1 :
                queue.append(temp1)
        return True 

