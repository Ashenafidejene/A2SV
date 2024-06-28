# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nums = []

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        small = root.val
        self.compareBuilder(root, small, small)
        return max(self.nums, default=0)
    
    def compareBuilder(self, root: Optional[TreeNode], small: int, larger: int):
        if root is None:
            return
        
        if root.right is not None:
            right = root.right
            val = right.val
            smaller = min(small, val)
            largerer = max(larger, val)
            difference = largerer - smaller
            self.nums.append(difference)
            self.compareBuilder(right, smaller, largerer)
        
        if root.left is not None:
            left = root.left
            val = left.val
            smaller = min(small, val)
            largerer = max(larger, val)
            difference = largerer - smaller
            self.nums.append(difference)
            self.compareBuilder(left, smaller, largerer)


        