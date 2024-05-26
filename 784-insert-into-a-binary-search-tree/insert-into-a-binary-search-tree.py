# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        if root is None:
            return newNode
        
        ptr = root
        while ptr is not None:
            if val < ptr.val:
                if ptr.left is None:
                    ptr.left = newNode
                    return root
                else:
                    ptr = ptr.left
            else:
                if ptr.right is None:
                    ptr.right = newNode
                    return root
                else:
                    ptr = ptr.right

        return root
     