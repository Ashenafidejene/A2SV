# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Use a dictionary to count frequencies
        freq = defaultdict(int)
        
        def count_freq(node: Optional[TreeNode]):
            if not node:
                return
            freq[node.val] += 1
            count_freq(node.left)
            count_freq(node.right)
        
        # Count the frequency of each value
        count_freq(root)
        
        # Find the maximum frequency
        max_freq = max(freq.values())
        
        # Collect all values with the maximum frequency
        modes = [val for val, count in freq.items() if count == max_freq]
        
        return modes