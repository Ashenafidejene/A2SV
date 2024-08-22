# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def dfs(node):
            if not node:
                return 0
            rightSum = dfs(node.right)
            leftSum = dfs(node.left)
            total = rightSum + leftSum + node.val
            ans.append(total)
            return total
        kk=dfs(root)
        counter = Counter(ans)
        most_common = counter.most_common()

        # Get the highest frequency
        highest_frequency = most_common[0][1]

        # Filter out the numbers that have the highest frequency
        most_frequent_numbers = [num for num, freq in most_common if freq == highest_frequency]
        return most_frequent_numbers
